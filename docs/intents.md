Implemented Intents:
```
{
  "intents": [
    {
      "intent": "DieRollSimple",
      "slots": [
        {
          "name": "NumDice",
          "type": "AMAZON.NUMBER"
        },
        {
          "name": "DieType",
          "type": "AMAZON.NUMBER"
        }
      ]
    },
    {
      "intent": "DieRollComplex",
      "slots": [
        {
          "name": "NumDice",
          "type": "AMAZON.NUMBER"
        },
        {
          "name": "DieType",
          "type": "AMAZON.NUMBER"
        },
        {
          "name": "ResultModification",
          "type": "AddOrSubtract"
        },
        {
          "name": "ResultModifier",
          "type": "AMAZON.NUMBER"
        },
        {
          "name": "DropModification",
          "type": "HighestOrLowest"
        },
        {
          "name": "DropNumber",
          "type": "AMAZON.NUMBER"
        }
      ]
    },
    {
      "intent": "AMAZON.HelpIntent"
    },
    {
      "intent": "AMAZON.StopIntent"
    },
    {
      "intent": "AMAZON.CancelIntent"
    }
  ]
}
