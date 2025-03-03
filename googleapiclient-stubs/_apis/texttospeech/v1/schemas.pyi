import typing

import typing_extensions

_list = list

@typing.type_check_only
class AudioConfig(typing_extensions.TypedDict, total=False):
    audioEncoding: typing_extensions.Literal[
        "AUDIO_ENCODING_UNSPECIFIED", "LINEAR16", "MP3", "OGG_OPUS", "MULAW", "ALAW"
    ]
    effectsProfileId: _list[str]
    pitch: float
    sampleRateHertz: int
    speakingRate: float
    volumeGainDb: float

@typing.type_check_only
class ImportDataRequest(typing_extensions.TypedDict, total=False):
    csvCloudStorageUri: str

@typing.type_check_only
class ListVoicesResponse(typing_extensions.TypedDict, total=False):
    voices: _list[Voice]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SynthesisInput(typing_extensions.TypedDict, total=False):
    ssml: str
    text: str

@typing.type_check_only
class SynthesizeSpeechRequest(typing_extensions.TypedDict, total=False):
    audioConfig: AudioConfig
    input: SynthesisInput
    voice: VoiceSelectionParams

@typing.type_check_only
class SynthesizeSpeechResponse(typing_extensions.TypedDict, total=False):
    audioContent: str

@typing.type_check_only
class Voice(typing_extensions.TypedDict, total=False):
    languageCodes: _list[str]
    name: str
    naturalSampleRateHertz: int
    ssmlGender: typing_extensions.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED", "MALE", "FEMALE", "NEUTRAL"
    ]

@typing.type_check_only
class VoiceSelectionParams(typing_extensions.TypedDict, total=False):
    languageCode: str
    name: str
    ssmlGender: typing_extensions.Literal[
        "SSML_VOICE_GENDER_UNSPECIFIED", "MALE", "FEMALE", "NEUTRAL"
    ]
