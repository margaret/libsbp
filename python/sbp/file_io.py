#!/usr/bin/env python
# Copyright (C) 2015 Swift Navigation Inc.
# Contact: Fergus Noble <fergus@swiftnav.com>
#
# This source is subject to the license found in the file 'LICENSE' which must
# be be distributed together with this source. All other rights reserved.
#
# THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.


"""
Messages for using device's onboard flash filesystem
functionality. This allows data to be stored persistently in the
device's program flash with wear-levelling using a simple filesystem
interface. The file system interface (CFS) defines an abstract API
for reading directories and for reading and writing files.

These are in the implementation-defined range (0x0000-0x00FF), and
intended for internal-use only. Note that some of these messages
share the same message type ID for both the host request and the
device response.

"""

from construct import *
import json
from sbp.msg import SBP, SENDER_ID
from sbp.utils import fmt_repr, exclude_fields, walk_json_dict, containerize, greedy_string

# Automatically generated from piksi/yaml/swiftnav/sbp/file_io.yaml with generate.py.
# Please do not hand edit!


SBP_MSG_FILEIO_READ_REQ = 0x00A8
class MsgFileioReadReq(SBP):
  """SBP class for message MSG_FILEIO_READ_REQ (0x00A8).

  You can have MSG_FILEIO_READ_REQ inherent its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  The file read message reads a certain length (up to 255 bytes)
from a given offset into a file, and returns the data in a
MSG_FILEIO_READ_RESP message where the message length field
indicates how many bytes were succesfully read. If the message is
invalid, a followup MSG_PRINT message will print "Invalid fileio
read message".


  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  offset : int
    File offset
  chunk_size : int
    Chunk size to read
  filename : string
    Name of the file to read from (NULL padded)
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("MsgFileioReadReq",
                   ULInt32('offset'),
                   ULInt8('chunk_size'),
                   String('filename', 20),)
  __slots__ = [
               'offset',
               'chunk_size',
               'filename',
              ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( MsgFileioReadReq,
             self).__init__(sbp.msg_type, sbp.sender, sbp.length,
                            sbp.payload, sbp.crc)
      self.from_binary(sbp.payload)
    else:
      super( MsgFileioReadReq, self).__init__()
      self.msg_type = SBP_MSG_FILEIO_READ_REQ
      self.sender = kwargs.pop('sender', SENDER_ID)
      self.offset = kwargs.pop('offset')
      self.chunk_size = kwargs.pop('chunk_size')
      self.filename = kwargs.pop('filename')

  def __repr__(self):
    return fmt_repr(self)
 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    p = MsgFileioReadReq._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = MsgFileioReadReq._parser.build(c)
    return self.pack()

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    sbp = SBP.from_json_dict(d)
    return MsgFileioReadReq(sbp)

  def to_json_dict(self):
    self.to_binary()
    d = super( MsgFileioReadReq, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    
SBP_MSG_FILEIO_READ_RESP = 0x00A3
class MsgFileioReadResp(SBP):
  """SBP class for message MSG_FILEIO_READ_RESP (0x00A3).

  You can have MSG_FILEIO_READ_RESP inherent its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  The file read message reads a certain length (up to 255 bytes)
from a given offset into a file, and returns the data in a
message where the message length field indicates how many bytes
were succesfully read.


  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  offset : int
    File offset
  chunk_size : int
    Chunk size read
  filename : string
    Name of the file read from (NULL padded)
  contents : array
    Contents of read file
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("MsgFileioReadResp",
                   ULInt32('offset'),
                   ULInt8('chunk_size'),
                   String('filename', 20),
                   OptionalGreedyRange(ULInt8('contents')),)
  __slots__ = [
               'offset',
               'chunk_size',
               'filename',
               'contents',
              ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( MsgFileioReadResp,
             self).__init__(sbp.msg_type, sbp.sender, sbp.length,
                            sbp.payload, sbp.crc)
      self.from_binary(sbp.payload)
    else:
      super( MsgFileioReadResp, self).__init__()
      self.msg_type = SBP_MSG_FILEIO_READ_RESP
      self.sender = kwargs.pop('sender', SENDER_ID)
      self.offset = kwargs.pop('offset')
      self.chunk_size = kwargs.pop('chunk_size')
      self.filename = kwargs.pop('filename')
      self.contents = kwargs.pop('contents')

  def __repr__(self):
    return fmt_repr(self)
 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    p = MsgFileioReadResp._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = MsgFileioReadResp._parser.build(c)
    return self.pack()

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    sbp = SBP.from_json_dict(d)
    return MsgFileioReadResp(sbp)

  def to_json_dict(self):
    self.to_binary()
    d = super( MsgFileioReadResp, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    
SBP_MSG_FILEIO_READ_DIR_REQ = 0x00A9
class MsgFileioReadDirReq(SBP):
  """SBP class for message MSG_FILEIO_READ_DIR_REQ (0x00A9).

  You can have MSG_FILEIO_READ_DIR_REQ inherent its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  The read directory message lists the files in a directory on the
device's onboard flash file system.  The offset parameter can be
used to skip the first n elements of the file list. Returns a
MSG_FILEIO_READ_DIR_RESP message containing the directory
listings as a NULL delimited list. The listing is chunked over
multiple SBP packets and the end of the list is identified by an
entry containing just the character 0xFF. If message is invalid, a
followup MSG_PRINT message will print "Invalid fileio read
message".


  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  offset : int
    The offset to skip the first n elements of the file list

  dirname : string
    Name of the directory to list (NULL padded)
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("MsgFileioReadDirReq",
                   ULInt32('offset'),
                   String('dirname', 20),)
  __slots__ = [
               'offset',
               'dirname',
              ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( MsgFileioReadDirReq,
             self).__init__(sbp.msg_type, sbp.sender, sbp.length,
                            sbp.payload, sbp.crc)
      self.from_binary(sbp.payload)
    else:
      super( MsgFileioReadDirReq, self).__init__()
      self.msg_type = SBP_MSG_FILEIO_READ_DIR_REQ
      self.sender = kwargs.pop('sender', SENDER_ID)
      self.offset = kwargs.pop('offset')
      self.dirname = kwargs.pop('dirname')

  def __repr__(self):
    return fmt_repr(self)
 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    p = MsgFileioReadDirReq._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = MsgFileioReadDirReq._parser.build(c)
    return self.pack()

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    sbp = SBP.from_json_dict(d)
    return MsgFileioReadDirReq(sbp)

  def to_json_dict(self):
    self.to_binary()
    d = super( MsgFileioReadDirReq, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    
SBP_MSG_FILEIO_READ_DIR_RESP = 0x00AA
class MsgFileioReadDirResp(SBP):
  """SBP class for message MSG_FILEIO_READ_DIR_RESP (0x00AA).

  You can have MSG_FILEIO_READ_DIR_RESP inherent its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  The read directory message lists the files in a directory on the
device's onboard flash file system.  The offset parameter can be
used to skip the first n elements of the file list. Message contains
the directory listings as a NULL delimited list. The listing is
chunked over multiple SBP packets and the end of the list is
identified by an entry containing just the character 0xFF.


  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  offset : int
    The offset to skip the first n elements of the file list

  dirname : string
    Name of the directory to list (NULL padded)
  contents : array
    Contents of read directory
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("MsgFileioReadDirResp",
                   ULInt32('offset'),
                   String('dirname', 20),
                   OptionalGreedyRange(ULInt8('contents')),)
  __slots__ = [
               'offset',
               'dirname',
               'contents',
              ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( MsgFileioReadDirResp,
             self).__init__(sbp.msg_type, sbp.sender, sbp.length,
                            sbp.payload, sbp.crc)
      self.from_binary(sbp.payload)
    else:
      super( MsgFileioReadDirResp, self).__init__()
      self.msg_type = SBP_MSG_FILEIO_READ_DIR_RESP
      self.sender = kwargs.pop('sender', SENDER_ID)
      self.offset = kwargs.pop('offset')
      self.dirname = kwargs.pop('dirname')
      self.contents = kwargs.pop('contents')

  def __repr__(self):
    return fmt_repr(self)
 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    p = MsgFileioReadDirResp._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = MsgFileioReadDirResp._parser.build(c)
    return self.pack()

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    sbp = SBP.from_json_dict(d)
    return MsgFileioReadDirResp(sbp)

  def to_json_dict(self):
    self.to_binary()
    d = super( MsgFileioReadDirResp, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    
SBP_MSG_FILEIO_REMOVE = 0x00AC
class MsgFileioRemove(SBP):
  """SBP class for message MSG_FILEIO_REMOVE (0x00AC).

  You can have MSG_FILEIO_REMOVE inherent its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  The file remove message deletes a file from the file system. If
message is invalid, a followup MSG_PRINT message will print
"Invalid fileio remove message".


  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  filename : string
    Name of the file to delete (NULL padded)
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("MsgFileioRemove",
                   String('filename', 20),)
  __slots__ = [
               'filename',
              ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( MsgFileioRemove,
             self).__init__(sbp.msg_type, sbp.sender, sbp.length,
                            sbp.payload, sbp.crc)
      self.from_binary(sbp.payload)
    else:
      super( MsgFileioRemove, self).__init__()
      self.msg_type = SBP_MSG_FILEIO_REMOVE
      self.sender = kwargs.pop('sender', SENDER_ID)
      self.filename = kwargs.pop('filename')

  def __repr__(self):
    return fmt_repr(self)
 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    p = MsgFileioRemove._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = MsgFileioRemove._parser.build(c)
    return self.pack()

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    sbp = SBP.from_json_dict(d)
    return MsgFileioRemove(sbp)

  def to_json_dict(self):
    self.to_binary()
    d = super( MsgFileioRemove, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    
SBP_MSG_FILEIO_WRITE_REQ = 0x00AD
class MsgFileioWriteReq(SBP):
  """SBP class for message MSG_FILEIO_WRITE_REQ (0x00AD).

  You can have MSG_FILEIO_WRITE_REQ inherent its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  The file write message writes a certain length (up to 255 bytes)
of data to a file at a given offset. Returns a copy of the
original MSG_FILEIO_WRITE_RESP message to check integrity of
the write. If message is invalid, a followup MSG_PRINT message
will print "Invalid fileio write message".


  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  filename : string
    Name of the file to write to (NULL padded)
  offset : int
    Offset into the file at which to start writing in bytes
  data : array
    Variable-length array of data to write
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("MsgFileioWriteReq",
                   String('filename', 20),
                   ULInt32('offset'),
                   OptionalGreedyRange(ULInt8('data')),)
  __slots__ = [
               'filename',
               'offset',
               'data',
              ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( MsgFileioWriteReq,
             self).__init__(sbp.msg_type, sbp.sender, sbp.length,
                            sbp.payload, sbp.crc)
      self.from_binary(sbp.payload)
    else:
      super( MsgFileioWriteReq, self).__init__()
      self.msg_type = SBP_MSG_FILEIO_WRITE_REQ
      self.sender = kwargs.pop('sender', SENDER_ID)
      self.filename = kwargs.pop('filename')
      self.offset = kwargs.pop('offset')
      self.data = kwargs.pop('data')

  def __repr__(self):
    return fmt_repr(self)
 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    p = MsgFileioWriteReq._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = MsgFileioWriteReq._parser.build(c)
    return self.pack()

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    sbp = SBP.from_json_dict(d)
    return MsgFileioWriteReq(sbp)

  def to_json_dict(self):
    self.to_binary()
    d = super( MsgFileioWriteReq, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    
SBP_MSG_FILEIO_WRITE_RESP = 0x00AB
class MsgFileioWriteResp(SBP):
  """SBP class for message MSG_FILEIO_WRITE_RESP (0x00AB).

  You can have MSG_FILEIO_WRITE_RESP inherent its fields directly
  from an inherited SBP object, or construct it inline using a dict
  of its fields.

  
  The file write message writes a certain length (up to 255 bytes)
of data to a file at a given offset. The message is a copy of the
original MSG_FILEIO_WRITE_REQ message to check integrity of the
write.


  Parameters
  ----------
  sbp : SBP
    SBP parent object to inherit from.
  filename : string
    Name of the file to write to (NULL padded)
  offset : int
    Offset into the file at which to start writing in bytes
  data : array
    Variable-length array of data to write
  sender : int
    Optional sender ID, defaults to SENDER_ID (see sbp/msg.py).

  """
  _parser = Struct("MsgFileioWriteResp",
                   String('filename', 20),
                   ULInt32('offset'),
                   OptionalGreedyRange(ULInt8('data')),)
  __slots__ = [
               'filename',
               'offset',
               'data',
              ]

  def __init__(self, sbp=None, **kwargs):
    if sbp:
      super( MsgFileioWriteResp,
             self).__init__(sbp.msg_type, sbp.sender, sbp.length,
                            sbp.payload, sbp.crc)
      self.from_binary(sbp.payload)
    else:
      super( MsgFileioWriteResp, self).__init__()
      self.msg_type = SBP_MSG_FILEIO_WRITE_RESP
      self.sender = kwargs.pop('sender', SENDER_ID)
      self.filename = kwargs.pop('filename')
      self.offset = kwargs.pop('offset')
      self.data = kwargs.pop('data')

  def __repr__(self):
    return fmt_repr(self)
 
  def from_binary(self, d):
    """Given a binary payload d, update the appropriate payload fields of
    the message.

    """
    p = MsgFileioWriteResp._parser.parse(d)
    for n in self.__class__.__slots__:
      setattr(self, n, getattr(p, n))

  def to_binary(self):
    """Produce a framed/packed SBP message.

    """
    c = containerize(exclude_fields(self))
    self.payload = MsgFileioWriteResp._parser.build(c)
    return self.pack()

  @staticmethod
  def from_json(s):
    """Given a JSON-encoded string s, build a message object.

    """
    d = json.loads(s)
    sbp = SBP.from_json_dict(d)
    return MsgFileioWriteResp(sbp)

  def to_json_dict(self):
    self.to_binary()
    d = super( MsgFileioWriteResp, self).to_json_dict()
    j = walk_json_dict(exclude_fields(self))
    d.update(j)
    return d
    

msg_classes = {
  0x00A8: MsgFileioReadReq,
  0x00A3: MsgFileioReadResp,
  0x00A9: MsgFileioReadDirReq,
  0x00AA: MsgFileioReadDirResp,
  0x00AC: MsgFileioRemove,
  0x00AD: MsgFileioWriteReq,
  0x00AB: MsgFileioWriteResp,
}