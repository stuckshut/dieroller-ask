intent_request = dict({
  "session": {
    "sessionId": "SessionId.732c32a0-1efd-44c3-808c-6da8dd2ca8ab",
    "application": {
      "applicationId": "amzn1.echo-sdk-ams.app.43de1112-c924-46eb-b053-b8a410268e36"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.ask.account.AFP3ZWPOS2BGJR7OWJZ3DHPKMOMNWY4AY66FUR7ILBWANIHQN73QGGHLYDRCHM2MVDFODCVEJAV2TTB2AZLVTNAPFBXXDLXL7MR5A3EL4WE3H4TCXSDDY5VDZ6EZJMHZNXA74J2SL2QZH2MRFMPXE32SUEISZTVJWZJZMRTE2EQM4LAOHQ23JSMYBYAVSO656MQFLPFICU2ALZI"
    },
    "new": True
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId.92828a3c-8cbd-4bd4-a8a0-cb89a4012acb",
    "timestamp": "2016-07-15T07:13:35Z",
    "intent": {
      "name": "GetTeaInfo",
      "slots": {
        "TeaType": {
          "name": "TeaType",
          "value": "green"
        }
      }
    },
    "locale": "en-US"
  },
  "version": "1.0"
})


launch_request = dict({
    "session": {
        "sessionId": "SessionId.732c32a0-1efd-44c3-808c-6da8dd2ca8ab",
        "application": {
            "applicationId": "amzn1.echo-sdk-ams.app.43de1112-c924-46eb-b053-b8a410268e36"
        },
        "attributes": {},
        "user": {
            "userId": "amzn1.ask.account.AFP3ZWPOS2BGJR7OWJZ3DHPKMOMNWY4AY66FUR7ILBWANIHQN73QGGHLYDRCHM2MVDFODCVEJAV2TTB2AZLVTNAPFBXXDLXL7MR5A3EL4WE3H4TCXSDDY5VDZ6EZJMHZNXA74J2SL2QZH2MRFMPXE32SUEISZTVJWZJZMRTE2EQM4LAOHQ23JSMYBYAVSO656MQFLPFICU2ALZI"
        },
        "new": True
    },
    "request": {
        "type": "LaunchRequest",
        "requestId": "q4aua34ta34ata32ta",
        "timestamp": "2015-05-13T12:34:56Z"
    },
    "version": "1.0"
})


end_request = dict({
    "session": {
        "sessionId": "SessionId.732c32a0-1efd-44c3-808c-6da8dd2ca8ab",
        "application": {
            "applicationId": "amzn1.echo-sdk-ams.app.43de1112-c924-46eb-b053-b8a410268e36"
        },
        "attributes": {},
        "user": {
            "userId": "amzn1.ask.account.AFP3ZWPOS2BGJR7OWJZ3DHPKMOMNWY4AY66FUR7ILBWANIHQN73QGGHLYDRCHM2MVDFODCVEJAV2TTB2AZLVTNAPFBXXDLXL7MR5A3EL4WE3H4TCXSDDY5VDZ6EZJMHZNXA74J2SL2QZH2MRFMPXE32SUEISZTVJWZJZMRTE2EQM4LAOHQ23JSMYBYAVSO656MQFLPFICU2ALZI"
        },
        "new": True
    },
    "request": {
        "type": "SessionEndedRequest",
        "requestId": "asdfqw5us6d6jdj6s4e",
        "timestamp": "2015-05-13T12:34:56Z",
        "reason": "Reasons"
    },
    "version": "1.0"
})


help_request = dict({
    "session": {
        "sessionId": "SessionId.732c32a0-1efd-44c3-808c-6da8dd2ca8ab",
        "application": {
            "applicationId": "amzn1.echo-sdk-ams.app.43de1112-c924-46eb-b053-b8a410268e36"
        },
        "attributes": {},
        "user": {
            "userId": "amzn1.ask.account.AFP3ZWPOS2BGJR7OWJZ3DHPKMOMNWY4AY66FUR7ILBWANIHQN73QGGHLYDRCHM2MVDFODCVEJAV2TTB2AZLVTNAPFBXXDLXL7MR5A3EL4WE3H4TCXSDDY5VDZ6EZJMHZNXA74J2SL2QZH2MRFMPXE32SUEISZTVJWZJZMRTE2EQM4LAOHQ23JSMYBYAVSO656MQFLPFICU2ALZI"
        },
        "new": True
    },
    "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.92828a3c-8cbd-4bd4-a8a0-cb89a4012acb",
        "timestamp": "2016-07-15T07:13:35Z",
        "intent": {
            "name": "AMAZON.HelpIntent",
            "slots": {}
        },
        "locale": "en-US"
    },
    "version": "1.0"
})


stop_request = dict({
    "session": {
        "sessionId": "SessionId.732c32a0-1efd-44c3-808c-6da8dd2ca8ab",
        "application": {
            "applicationId": "amzn1.echo-sdk-ams.app.43de1112-c924-46eb-b053-b8a410268e36"
        },
        "attributes": {},
        "user": {
            "userId": "amzn1.ask.account.AFP3ZWPOS2BGJR7OWJZ3DHPKMOMNWY4AY66FUR7ILBWANIHQN73QGGHLYDRCHM2MVDFODCVEJAV2TTB2AZLVTNAPFBXXDLXL7MR5A3EL4WE3H4TCXSDDY5VDZ6EZJMHZNXA74J2SL2QZH2MRFMPXE32SUEISZTVJWZJZMRTE2EQM4LAOHQ23JSMYBYAVSO656MQFLPFICU2ALZI"
        },
        "new": True
    },
    "request": {
        "type": "IntentRequest",
        "requestId": "EdwRequestId.92828a3c-8cbd-4bd4-a8a0-cb89a4012acb",
        "timestamp": "2016-07-15T07:13:35Z",
        "intent": {
            "name": "AMAZON.StopIntent",
            "slots": {}
        },
        "locale": "en-US"
    },
    "version": "1.0"
})
