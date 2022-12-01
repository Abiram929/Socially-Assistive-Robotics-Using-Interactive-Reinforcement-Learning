import random

def positive_gestures():
    BigSmile=["BigSmile", 0]
    Nod=["Nod", 0]
    Oh=["Oh", 0]
    Smile=["Smile", 0]
    Surprise=["Surprise", 0]
    Thoughtful=["Thoughtful", 0]
    Wink=["Wink", 0]
    
    Custom1= [{
    "frames": [
        {
            "time": [
                0.7
            ],
            "params": {
                "BLINK_LEFT": 1.0,
                "SMILE_CLOSED":0.7
            }
        },
        {
            "time": [
                0.67
            ],
            "params": {
                "reset": True
            }
        }
    ],
    "class": "furhatos.gestures.Gesture"
    },1]
    
    Custom2=[{
  "frames": [
    {
      "time": [
        0.17, 1.0, 6.0
      ],
      "params": {
        "NECK_ROLL": 25.0,
        "NECK_PAN": -12.0,
        "NECK_TILT": -25.0,
        "SMILE_OPEN": 0.7
      }
    },
    {
        "time": [
            3.0
        ],
        "params": { 
            "reset": True
        }
    }
  ],
  "class": "furhatos.gestures.Gesture"
},1]
    
    Custom3=[{
  "frames": [
    {
      "time": [
        0.17, 1.0
      ],
      "params": {
        "EXPR_FEAR": 1,
        "SMILE_OPEN": 0.7
      }
    },
    {
        "time": [
            3.0
        ],
        "params": { 
            "reset": True
        }
    }
  ],
  "class": "furhatos.gestures.Gesture"
}, 1]
    
    Custom4=[{
  "frames": [
    {
      "time": [
        0.17, 1.0
      ],
      "params": {
        "SMILE_OPEN": 1,
        "SUPRISED": 0.7
      }
    },
    {
        "time": [
            2.0
        ],
        "params": { 
            "reset": True
        }
    }
  ],
  "class": "furhatos.gestures.Gesture"
}, 1]
    
    all_gestures=[BigSmile, Nod, Oh, Smile, Surprise, Thoughtful, Wink, Custom1, Custom2, Custom3, Custom4]
    
    return random.choice(all_gestures)

def neutral_gestures():
    Blink=["Blink", 0]
    BrowFrown=["BrowFrown", 0]
    BrowRaise=["BrowRaise", 0]
    GazeAway=["GazeAway", 0]
    Nod=["Nod", 0]
    Roll=["Roll", 0]
    Shake=["Shake", 0]
    
    Custom1=[{
  "frames": [
    {
      "time": [
        1
      ],
      "params": {
        "PHONE_OOH_Q": 1,
        "PHONE_CH_J_SH": 1,
        "BROW_IN_RIGHT": 1
      }
    },
    {
        "time": [
            2.0
        ],
        "params": { 
            "reset": True
        }
    }
  ],
  "class": "furhatos.gestures.Gesture"
}, 1]
    
    Custom2=[{
  "frames": [
    {
      "time": [
        1
      ],
      "params": {
        "EYE_SQUINT_LEFT": 1,
        "EYE_SQUINT_RIGHT": 1,
        "SMILE_CLOSED": 0.1,
        "GAZE_TILT": 40  
      }
    },
    {
        "time": [
            2.0
        ],
        "params": { 
            "reset": True
        }
    }
  ],
  "class": "furhatos.gestures.Gesture"
}, 1]
    
    Custom3=[{
  "frames": [
    {
      "time": [
        1
      ],
      "params": {
        "BROW_IN_LEFT": 1,
        "BROW_UP_RIGHT": 1,
        "GAZE_TILT": 50,
        "NECK_ROLL": 50
      }
    },
    {
        "time": [
            2.0
        ],
        "params": { 
            "reset": True
        }
    }
  ],
  "class": "furhatos.gestures.Gesture"
}, 1]
    
    all_gestures=[Blink, BrowFrown, BrowRaise, GazeAway, Nod, Roll, Shake, Custom1, Custom2, Custom3]
    
    return random.choice(all_gestures)


def negative_gestures():
    ExpressAnger=["ExpressAnger", 0]
    ExpressDisgust=["ExpressDisgust", 0]
    ExpressFear=["ExpressFear", 0]
    ExpressSad=["ExpressSad", 0]
    
    Custom1=[{
  "frames": [
    {
      "time": [
        1
      ],
      "params": {
        "EXPR_ANGER": 1,
        "BROW_IN_LEFT": 1,
        "BROW_UP_RIGHT": 1,
        "GAZE_TILT": 50,
        "NECK_ROLL": 50
      }
    },
    {
        "time": [
            2.0
        ],
        "params": { 
            "reset": True
        }
    }
  ],
  "class": "furhatos.gestures.Gesture"
}, 1]
    
    Custom2=[{
  "frames": [
    {
      "time": [
        1
      ],
      "params": {
        "EXPR_DISGUST": 1,
        "EXPR_FEAR": 1,
        "EYE_SQUINT_LEFT": 1
      }
    },
    {
        "time": [
            2.0
        ],
        "params": { 
            "reset": True
        }
    }
  ],
  "class": "furhatos.gestures.Gesture"
}, 1]
    
    Custom3=[{
  "frames": [
    {
      "time": [
        1
      ],
      "params": {
        "EXPR_DISGUST": 1,
        "EXPR_FEAR": 1,
        "EXPR_SAD": 1,
        "NECK_TILT": 10
      }
    },
    {
        "time": [
            2.0
        ],
        "params": { 
            "reset": True
        }
    }
  ],
  "class": "furhatos.gestures.Gesture"
}, 1]
    
    Custom4=[{
  "frames": [
    {
      "time": [
        1
      ],
      "params": {
        "EXPR_ANGER":1,
        "EYE_SQUINT_RIGHT":1,
        "SURPRISE":1,
        "NECK_ROLL":-50
          
      }
    },
    {
        "time": [
            2.0
        ],
        "params": { 
            "reset": True
        }
    }
  ],
  "class": "furhatos.gestures.Gesture"
}, 1]
    
    all_gestures=[ExpressAnger, ExpressDisgust, ExpressFear, ExpressSad, Custom1, Custom2, Custom3, Custom4]
    
    return random.choice(all_gestures)

def generate_gestures(valence):
    if valence == 2:
        return positive_gestures()
    elif valence == 1:
        return neutral_gestures()
    else:
        return negative_gestures()
    
    
    