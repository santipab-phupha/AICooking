# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PartiiService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13PartiiService.proto\x12\x06partii\"\x17\n\x04Word\x12\x0f\n\x07wordstr\x18\x01 \x01(\t\"-\n\nWordResult\x12\x0e\n\x06wordid\x18\x01 \x01(\x03\x12\x0f\n\x07wordstr\x18\x02 \x01(\t\"\n\n\x08\x45mptyMsg\"(\n\x13\x41vailableConnection\x12\x11\n\tAvailable\x18\x01 \x01(\x03\" \n\x0b\x42uildNumber\x12\x11\n\tBuildDate\x18\x01 \x01(\t\"Q\n\x08\x41uthData\x12\x0e\n\x06\x41piKey\x18\x01 \x01(\t\x12\x14\n\x0cSamplingRate\x18\x02 \x01(\x03\x12\x10\n\x08\x43lientID\x18\x03 \x01(\t\x12\r\n\x05\x43odec\x18\x04 \x01(\x03\"E\n\nAuthStatus\x12\x0f\n\x07Message\x18\x01 \x01(\t\x12&\n\nAuthStatus\x18\x02 \x01(\x0e\x32\x12.partii.StatusCode\"X\n\tAudioData\x12\x11\n\tByteChunk\x18\x01 \x01(\x0c\x12\x0f\n\x07\x42ytelen\x18\x02 \x01(\x03\x12\'\n\x08\x44\x61tatype\x18\x03 \x01(\x0e\x32\x15.partii.AudioDataType\"\x8b\x01\n\nWordsLevel\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x11\n\tstartTime\x18\x03 \x01(\x02\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x02\x12\x12\n\nwordNumber\x18\x05 \x01(\x03\x12#\n\x06phones\x18\x06 \x03(\x0b\x32\x13.partii.PhonesLevel\"i\n\x0bPhonesLevel\x12\r\n\x05phone\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x11\n\tstartTime\x18\x03 \x01(\x02\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x02\x12\x13\n\x0bphoneNumber\x18\x05 \x01(\x03\"\xba\x02\n\x13TranscriptionResult\x12\x12\n\ntranscript\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x11\n\tstartTime\x18\x03 \x01(\x02\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x02\x12\x16\n\x0esentenceNumber\x18\x05 \x01(\x03\x12(\n\x0csentenceType\x18\x06 \x01(\x0e\x32\x12.partii.ResultType\x12!\n\x05words\x18\x07 \x03(\x0b\x32\x12.partii.WordsLevel\x12&\n\x07\x65motion\x18\x08 \x01(\x0b\x32\x15.partii.EmotionResult\x12&\n\x07speaker\x18\t \x01(\x0b\x32\x15.partii.SpeakerResult\x12\"\n\x06Status\x18\n \x01(\x0e\x32\x12.partii.StatusCode\"\xaa\x01\n\rSpeakerResult\x12\x11\n\tspeakerID\x18\x01 \x01(\x03\x12\x11\n\tstartTime\x18\x02 \x01(\x02\x12\x0f\n\x07\x65ndTime\x18\x03 \x01(\x02\x12\x15\n\rspeakerNumber\x18\x04 \x01(\x03\x12\'\n\x0bspeakerType\x18\x05 \x01(\x0e\x32\x12.partii.ResultType\x12\"\n\x06Status\x18\x06 \x01(\x0e\x32\x12.partii.StatusCode\"\xe5\x01\n\rEmotionResult\x12\x0f\n\x07\x65motion\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x11\n\tstartTime\x18\x03 \x01(\x02\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x02\x12\x15\n\remotionNumber\x18\x05 \x01(\x03\x12\'\n\x0bsegmentType\x18\x06 \x01(\x0e\x32\x12.partii.ResultType\x12\'\n\x0bsubemotions\x18\x07 \x03(\x0b\x32\x12.partii.SubEmotion\x12\"\n\x06Status\x18\x08 \x01(\x0e\x32\x12.partii.StatusCode\"l\n\nSubEmotion\x12\x0f\n\x07\x65motion\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x11\n\tstartTime\x18\x03 \x01(\x02\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x02\x12\x15\n\remotionNumber\x18\x05 \x01(\x03\"X\n\x07VADProb\x12\x0f\n\x07\x66rameid\x18\x01 \x01(\x03\x12\x13\n\x0bprobability\x18\x02 \x01(\x02\x12\'\n\x08\x64\x61tatype\x18\x03 \x01(\x0e\x32\x15.partii.AudioDataType\"n\n\x12\x43\x61librateVadResult\x12\x14\n\x0cvadthreshold\x18\x01 \x01(\x02\x12\x1e\n\x05probs\x18\x02 \x03(\x0b\x32\x0f.partii.VADProb\x12\"\n\x06Status\x18\x03 \x01(\x0e\x32\x12.partii.StatusCode\"\xbc\x01\n\x0eWakeWordResult\x12\x0c\n\x04word\x18\x01 \x01(\t\x12\x12\n\nconfidence\x18\x02 \x01(\x02\x12\x11\n\tstartTime\x18\x03 \x01(\x02\x12\x0f\n\x07\x65ndTime\x18\x04 \x01(\x02\x12\x16\n\x0ewakewordNumber\x18\x05 \x01(\x03\x12(\n\x0csentenceType\x18\x06 \x01(\x0e\x32\x12.partii.ResultType\x12\"\n\x06Status\x18\x07 \x01(\x0e\x32\x12.partii.StatusCode\"\xda\x01\n\x1eWakeWordAndTranscriptionResult\x12/\n\ntranscript\x18\x01 \x01(\x0b\x32\x1b.partii.TranscriptionResult\x12(\n\x08wakeword\x18\x02 \x01(\x0b\x32\x16.partii.WakeWordResult\x12&\n\nresulttype\x18\x03 \x01(\x0e\x32\x12.partii.ResultType\x12\"\n\x06Status\x18\x04 \x01(\x0e\x32\x12.partii.StatusCode\x12\x11\n\tstatusmsg\x18\x05 \x01(\t*f\n\nAudioCodec\x12\x0c\n\x08LINEAR16\x10\x00\x12\t\n\x05SPEEX\x10\x01\x12\x08\n\x04\x46LAC\x10\x02\x12\x07\n\x03MP3\x10\x03\x12\t\n\x05MULAW\x10\x04\x12\x07\n\x03\x41MR\x10\x05\x12\n\n\x06\x41MR_WB\x10\x06\x12\x0c\n\x08OGG_OPUS\x10\x07*Q\n\nResultType\x12\x0b\n\x07PARTIAL\x10\x00\x12\n\n\x06RESULT\x10\x01\x12\x0c\n\x08\x46INISHED\x10\x02\x12\x0c\n\x08WAKEWORD\x10\x03\x12\x0e\n\nTRANSCRIPT\x10\x04*8\n\rAudioDataType\x12\n\n\x06SPEECH\x10\x00\x12\r\n\tNONSPEECH\x10\x01\x12\x0c\n\x08\x45NDPOINT\x10\x02*-\n\nStatusCode\x12\x0b\n\x07Unknown\x10\x00\x12\x06\n\x02Ok\x10\x01\x12\n\n\x06\x46\x61iled\x10\x02\x32\x9d\x02\n\rTranscription\x12H\n\x10SingleTranscribe\x12\x11.partii.AudioData\x1a\x1b.partii.TranscriptionResult\"\x00(\x01\x30\x01\x12\x46\n\x0eLiveTranscribe\x12\x11.partii.AudioData\x1a\x1b.partii.TranscriptionResult\"\x00(\x01\x30\x01\x12?\n\x0cGetAvailable\x12\x10.partii.EmptyMsg\x1a\x1b.partii.AvailableConnection\"\x00\x12\x39\n\x0eGetBuildNumber\x12\x10.partii.EmptyMsg\x1a\x13.partii.BuildNumber\"\x00\x42\r\n\x0bpartii.grpcb\x06proto3')

_AUDIOCODEC = DESCRIPTOR.enum_types_by_name['AudioCodec']
AudioCodec = enum_type_wrapper.EnumTypeWrapper(_AUDIOCODEC)
_RESULTTYPE = DESCRIPTOR.enum_types_by_name['ResultType']
ResultType = enum_type_wrapper.EnumTypeWrapper(_RESULTTYPE)
_AUDIODATATYPE = DESCRIPTOR.enum_types_by_name['AudioDataType']
AudioDataType = enum_type_wrapper.EnumTypeWrapper(_AUDIODATATYPE)
_STATUSCODE = DESCRIPTOR.enum_types_by_name['StatusCode']
StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
LINEAR16 = 0
SPEEX = 1
FLAC = 2
MP3 = 3
MULAW = 4
AMR = 5
AMR_WB = 6
OGG_OPUS = 7
PARTIAL = 0
RESULT = 1
FINISHED = 2
WAKEWORD = 3
TRANSCRIPT = 4
SPEECH = 0
NONSPEECH = 1
ENDPOINT = 2
Unknown = 0
Ok = 1
Failed = 2


_WORD = DESCRIPTOR.message_types_by_name['Word']
_WORDRESULT = DESCRIPTOR.message_types_by_name['WordResult']
_EMPTYMSG = DESCRIPTOR.message_types_by_name['EmptyMsg']
_AVAILABLECONNECTION = DESCRIPTOR.message_types_by_name['AvailableConnection']
_BUILDNUMBER = DESCRIPTOR.message_types_by_name['BuildNumber']
_AUTHDATA = DESCRIPTOR.message_types_by_name['AuthData']
_AUTHSTATUS = DESCRIPTOR.message_types_by_name['AuthStatus']
_AUDIODATA = DESCRIPTOR.message_types_by_name['AudioData']
_WORDSLEVEL = DESCRIPTOR.message_types_by_name['WordsLevel']
_PHONESLEVEL = DESCRIPTOR.message_types_by_name['PhonesLevel']
_TRANSCRIPTIONRESULT = DESCRIPTOR.message_types_by_name['TranscriptionResult']
_SPEAKERRESULT = DESCRIPTOR.message_types_by_name['SpeakerResult']
_EMOTIONRESULT = DESCRIPTOR.message_types_by_name['EmotionResult']
_SUBEMOTION = DESCRIPTOR.message_types_by_name['SubEmotion']
_VADPROB = DESCRIPTOR.message_types_by_name['VADProb']
_CALIBRATEVADRESULT = DESCRIPTOR.message_types_by_name['CalibrateVadResult']
_WAKEWORDRESULT = DESCRIPTOR.message_types_by_name['WakeWordResult']
_WAKEWORDANDTRANSCRIPTIONRESULT = DESCRIPTOR.message_types_by_name['WakeWordAndTranscriptionResult']
Word = _reflection.GeneratedProtocolMessageType('Word', (_message.Message,), {
  'DESCRIPTOR' : _WORD,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.Word)
  })
_sym_db.RegisterMessage(Word)

WordResult = _reflection.GeneratedProtocolMessageType('WordResult', (_message.Message,), {
  'DESCRIPTOR' : _WORDRESULT,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.WordResult)
  })
_sym_db.RegisterMessage(WordResult)

EmptyMsg = _reflection.GeneratedProtocolMessageType('EmptyMsg', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYMSG,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.EmptyMsg)
  })
_sym_db.RegisterMessage(EmptyMsg)

AvailableConnection = _reflection.GeneratedProtocolMessageType('AvailableConnection', (_message.Message,), {
  'DESCRIPTOR' : _AVAILABLECONNECTION,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.AvailableConnection)
  })
_sym_db.RegisterMessage(AvailableConnection)

BuildNumber = _reflection.GeneratedProtocolMessageType('BuildNumber', (_message.Message,), {
  'DESCRIPTOR' : _BUILDNUMBER,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.BuildNumber)
  })
_sym_db.RegisterMessage(BuildNumber)

AuthData = _reflection.GeneratedProtocolMessageType('AuthData', (_message.Message,), {
  'DESCRIPTOR' : _AUTHDATA,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.AuthData)
  })
_sym_db.RegisterMessage(AuthData)

AuthStatus = _reflection.GeneratedProtocolMessageType('AuthStatus', (_message.Message,), {
  'DESCRIPTOR' : _AUTHSTATUS,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.AuthStatus)
  })
_sym_db.RegisterMessage(AuthStatus)

AudioData = _reflection.GeneratedProtocolMessageType('AudioData', (_message.Message,), {
  'DESCRIPTOR' : _AUDIODATA,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.AudioData)
  })
_sym_db.RegisterMessage(AudioData)

WordsLevel = _reflection.GeneratedProtocolMessageType('WordsLevel', (_message.Message,), {
  'DESCRIPTOR' : _WORDSLEVEL,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.WordsLevel)
  })
_sym_db.RegisterMessage(WordsLevel)

PhonesLevel = _reflection.GeneratedProtocolMessageType('PhonesLevel', (_message.Message,), {
  'DESCRIPTOR' : _PHONESLEVEL,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.PhonesLevel)
  })
_sym_db.RegisterMessage(PhonesLevel)

TranscriptionResult = _reflection.GeneratedProtocolMessageType('TranscriptionResult', (_message.Message,), {
  'DESCRIPTOR' : _TRANSCRIPTIONRESULT,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.TranscriptionResult)
  })
_sym_db.RegisterMessage(TranscriptionResult)

SpeakerResult = _reflection.GeneratedProtocolMessageType('SpeakerResult', (_message.Message,), {
  'DESCRIPTOR' : _SPEAKERRESULT,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.SpeakerResult)
  })
_sym_db.RegisterMessage(SpeakerResult)

EmotionResult = _reflection.GeneratedProtocolMessageType('EmotionResult', (_message.Message,), {
  'DESCRIPTOR' : _EMOTIONRESULT,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.EmotionResult)
  })
_sym_db.RegisterMessage(EmotionResult)

SubEmotion = _reflection.GeneratedProtocolMessageType('SubEmotion', (_message.Message,), {
  'DESCRIPTOR' : _SUBEMOTION,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.SubEmotion)
  })
_sym_db.RegisterMessage(SubEmotion)

VADProb = _reflection.GeneratedProtocolMessageType('VADProb', (_message.Message,), {
  'DESCRIPTOR' : _VADPROB,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.VADProb)
  })
_sym_db.RegisterMessage(VADProb)

CalibrateVadResult = _reflection.GeneratedProtocolMessageType('CalibrateVadResult', (_message.Message,), {
  'DESCRIPTOR' : _CALIBRATEVADRESULT,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.CalibrateVadResult)
  })
_sym_db.RegisterMessage(CalibrateVadResult)

WakeWordResult = _reflection.GeneratedProtocolMessageType('WakeWordResult', (_message.Message,), {
  'DESCRIPTOR' : _WAKEWORDRESULT,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.WakeWordResult)
  })
_sym_db.RegisterMessage(WakeWordResult)

WakeWordAndTranscriptionResult = _reflection.GeneratedProtocolMessageType('WakeWordAndTranscriptionResult', (_message.Message,), {
  'DESCRIPTOR' : _WAKEWORDANDTRANSCRIPTIONRESULT,
  '__module__' : 'PartiiService_pb2'
  # @@protoc_insertion_point(class_scope:partii.WakeWordAndTranscriptionResult)
  })
_sym_db.RegisterMessage(WakeWordAndTranscriptionResult)

_TRANSCRIPTION = DESCRIPTOR.services_by_name['Transcription']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\013partii.grpc'
  _AUDIOCODEC._serialized_start=2130
  _AUDIOCODEC._serialized_end=2232
  _RESULTTYPE._serialized_start=2234
  _RESULTTYPE._serialized_end=2315
  _AUDIODATATYPE._serialized_start=2317
  _AUDIODATATYPE._serialized_end=2373
  _STATUSCODE._serialized_start=2375
  _STATUSCODE._serialized_end=2420
  _WORD._serialized_start=31
  _WORD._serialized_end=54
  _WORDRESULT._serialized_start=56
  _WORDRESULT._serialized_end=101
  _EMPTYMSG._serialized_start=103
  _EMPTYMSG._serialized_end=113
  _AVAILABLECONNECTION._serialized_start=115
  _AVAILABLECONNECTION._serialized_end=155
  _BUILDNUMBER._serialized_start=157
  _BUILDNUMBER._serialized_end=189
  _AUTHDATA._serialized_start=191
  _AUTHDATA._serialized_end=272
  _AUTHSTATUS._serialized_start=274
  _AUTHSTATUS._serialized_end=343
  _AUDIODATA._serialized_start=345
  _AUDIODATA._serialized_end=433
  _WORDSLEVEL._serialized_start=436
  _WORDSLEVEL._serialized_end=575
  _PHONESLEVEL._serialized_start=577
  _PHONESLEVEL._serialized_end=682
  _TRANSCRIPTIONRESULT._serialized_start=685
  _TRANSCRIPTIONRESULT._serialized_end=999
  _SPEAKERRESULT._serialized_start=1002
  _SPEAKERRESULT._serialized_end=1172
  _EMOTIONRESULT._serialized_start=1175
  _EMOTIONRESULT._serialized_end=1404
  _SUBEMOTION._serialized_start=1406
  _SUBEMOTION._serialized_end=1514
  _VADPROB._serialized_start=1516
  _VADPROB._serialized_end=1604
  _CALIBRATEVADRESULT._serialized_start=1606
  _CALIBRATEVADRESULT._serialized_end=1716
  _WAKEWORDRESULT._serialized_start=1719
  _WAKEWORDRESULT._serialized_end=1907
  _WAKEWORDANDTRANSCRIPTIONRESULT._serialized_start=1910
  _WAKEWORDANDTRANSCRIPTIONRESULT._serialized_end=2128
  _TRANSCRIPTION._serialized_start=2423
  _TRANSCRIPTION._serialized_end=2708
# @@protoc_insertion_point(module_scope)
