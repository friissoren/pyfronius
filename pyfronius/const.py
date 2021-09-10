"""Constants for pyfronius."""

INVERTER_DEVICE_TYPE = {
    1: {"manufacturer": "Fronius", "model": "Gen24"},
    67: {"manufacturer": "Fronius", "model": "Primo 15.0-1 208-240"},
    68: {"manufacturer": "Fronius", "model": "Primo 12.5-1 208-240"},
    69: {"manufacturer": "Fronius", "model": "Primo 11.4-1 208-240"},
    70: {"manufacturer": "Fronius", "model": "Primo 10.0-1 208-240"},
    71: {"manufacturer": "Fronius", "model": "Symo 15.0-3 208"},
    72: {"manufacturer": "Fronius", "model": "Eco 27.0-3-S"},
    73: {"manufacturer": "Fronius", "model": "Eco 25.0-3-S"},
    75: {"manufacturer": "Fronius", "model": "Primo 6.0-1"},
    76: {"manufacturer": "Fronius", "model": "Primo 5.0-1"},
    77: {"manufacturer": "Fronius", "model": "Primo 4.6-1"},
    78: {"manufacturer": "Fronius", "model": "Primo 4.0-1"},
    79: {"manufacturer": "Fronius", "model": "Primo 3.6-1"},
    80: {"manufacturer": "Fronius", "model": "Primo 3.5-1"},
    81: {"manufacturer": "Fronius", "model": "Primo 3.0-1"},
    82: {"manufacturer": "Fronius", "model": "Symo Hybrid 4.0-3-S"},
    83: {"manufacturer": "Fronius", "model": "Symo Hybrid 3.0-3-S"},
    84: {"manufacturer": "Fronius", "model": "IG Plus 120 V-1"},
    85: {"manufacturer": "Fronius", "model": "Primo 3.8-1 208-240"},
    86: {"manufacturer": "Fronius", "model": "Primo 5.0-1 208-240"},
    87: {"manufacturer": "Fronius", "model": "Primo 6.0-1 208-240"},
    88: {"manufacturer": "Fronius", "model": "Primo 7.6-1 208-240"},
    89: {"manufacturer": "Fronius", "model": "Symo 24.0-3 USA Dummy"},
    90: {"manufacturer": "Fronius", "model": "Symo 24.0-3 480"},
    91: {"manufacturer": "Fronius", "model": "Symo 22.7-3 480"},
    92: {"manufacturer": "Fronius", "model": "Symo 20.0-3 480"},
    93: {"manufacturer": "Fronius", "model": "Symo 17.5-3 480"},
    94: {"manufacturer": "Fronius", "model": "Symo 15.0-3 480"},
    95: {"manufacturer": "Fronius", "model": "Symo 12.5-3 480"},
    96: {"manufacturer": "Fronius", "model": "Symo 10.0-3 480"},
    97: {"manufacturer": "Fronius", "model": "Symo 12.0-3 208-240"},
    98: {"manufacturer": "Fronius", "model": "Symo 10.0-3 208-240"},
    99: {"manufacturer": "Fronius", "model": "Symo Hybrid 5.0-3-S"},
    100: {"manufacturer": "Fronius", "model": "Primo 8.2-1 Dummy"},
    101: {"manufacturer": "Fronius", "model": "Primo 8.2-1 208-240"},
    102: {"manufacturer": "Fronius", "model": "Primo 8.2-1"},
    103: {"manufacturer": "Fronius", "model": "Agilo TL 360.0-3"},
    104: {"manufacturer": "Fronius", "model": "Agilo TL 460.0-3"},
    105: {"manufacturer": "Fronius", "model": "Symo 7.0-3-M"},
    106: {"manufacturer": "Fronius", "model": "Galvo 3.1-1 208-240"},
    107: {"manufacturer": "Fronius", "model": "Galvo 2.5-1 208-240"},
    108: {"manufacturer": "Fronius", "model": "Galvo 2.0-1 208-240"},
    109: {"manufacturer": "Fronius", "model": "Galvo 1.5-1 208-240"},
    110: {"manufacturer": "Fronius", "model": "Symo 6.0-3-M"},
    111: {"manufacturer": "Fronius", "model": "Symo 4.5-3-M"},
    112: {"manufacturer": "Fronius", "model": "Symo 3.7-3-M"},
    113: {"manufacturer": "Fronius", "model": "Symo 3.0-3-M"},
    114: {"manufacturer": "Fronius", "model": "Symo 17.5-3-M"},
    115: {"manufacturer": "Fronius", "model": "Symo 15.0-3-M"},
    116: {"manufacturer": "Fronius", "model": "Agilo 75.0-3 Outdoor"},
    117: {"manufacturer": "Fronius", "model": "Agilo 100.0-3 Outdoor"},
    118: {"manufacturer": "Fronius", "model": "IG Plus 55 V-1"},
    119: {"manufacturer": "Fronius", "model": "IG Plus 55 V-2"},
    120: {"manufacturer": "Fronius", "model": "Symo 20.0-3 Dummy"},
    121: {"manufacturer": "Fronius", "model": "Symo 20.0-3-M"},
    122: {"manufacturer": "Fronius", "model": "Symo 5.0-3-M"},
    123: {"manufacturer": "Fronius", "model": "Symo 8.2-3-M"},
    124: {"manufacturer": "Fronius", "model": "Symo 6.7-3-M"},
    125: {"manufacturer": "Fronius", "model": "Symo 5.5-3-M"},
    126: {"manufacturer": "Fronius", "model": "Symo 4.5-3-S"},
    127: {"manufacturer": "Fronius", "model": "Symo 3.7-3-S"},
    128: {"manufacturer": "Fronius", "model": "IG Plus 60 V-2"},
    129: {"manufacturer": "Fronius", "model": "IG Plus 60 V-1"},
    130: {"manufacturer": "SunPower", "model": "SPR 8001F-3 EU"},
    131: {"manufacturer": "Fronius", "model": "IG Plus 25 V-1"},
    132: {"manufacturer": "Fronius", "model": "IG Plus 100 V-3"},
    133: {"manufacturer": "Fronius", "model": "Agilo 100.0-3"},
    134: {"manufacturer": "SunPower", "model": "SPR 3001F-1 EU"},
    135: {"manufacturer": "Fronius", "model": "IG Plus V/A 10.0-3 Delta"},
    136: {"manufacturer": "Fronius", "model": "IG 50"},
    137: {"manufacturer": "Fronius", "model": "IG Plus 30 V-1"},
    138: {"manufacturer": "SunPower", "model": "SPR-11401f-1 UNI"},
    139: {"manufacturer": "SunPower", "model": "SPR-12001f-3 WYE277"},
    140: {"manufacturer": "SunPower", "model": "SPR-11401f-3 Delta"},
    141: {"manufacturer": "SunPower", "model": "SPR-10001f-1 UNI"},
    142: {"manufacturer": "SunPower", "model": "SPR-7501f-1 UNI"},
    143: {"manufacturer": "SunPower", "model": "SPR-6501f-1 UNI"},
    144: {"manufacturer": "SunPower", "model": "SPR-3801f-1 UNI"},
    145: {"manufacturer": "SunPower", "model": "SPR-3301f-1 UNI"},
    146: {"manufacturer": "SunPower", "model": "SPR 12001F-3 EU"},
    147: {"manufacturer": "SunPower", "model": "SPR 10001F-3 EU"},
    148: {"manufacturer": "SunPower", "model": "SPR 8001F-2 EU"},
    149: {"manufacturer": "SunPower", "model": "SPR 6501F-2 EU"},
    150: {"manufacturer": "SunPower", "model": "SPR 4001F-1 EU"},
    151: {"manufacturer": "SunPower", "model": "SPR 3501F-1 EU"},
    152: {"manufacturer": "Fronius", "model": "CL 60.0 WYE277 Dummy"},
    153: {"manufacturer": "Fronius", "model": "CL 55.5 Delta Dummy"},
    154: {"manufacturer": "Fronius", "model": "CL 60.0 Dummy"},
    155: {"manufacturer": "Fronius", "model": "IG Plus V 12.0-3 Dummy"},
    156: {"manufacturer": "Fronius", "model": "IG Plus V 7.5-1 Dummy"},
    157: {"manufacturer": "Fronius", "model": "IG Plus V 3.8-1 Dummy"},
    158: {"manufacturer": "Fronius", "model": "IG Plus 150 V-3 Dummy"},
    159: {"manufacturer": "Fronius", "model": "IG Plus 100 V-2 Dummy"},
    160: {"manufacturer": "Fronius", "model": "IG Plus 50 V-1 Dummy"},
    161: {"manufacturer": "Fronius", "model": "IG Plus V/A 12.0-3 WYE"},
    162: {"manufacturer": "Fronius", "model": "IG Plus V/A 11.4-3 Delta"},
    163: {"manufacturer": "Fronius", "model": "IG Plus V/A 11.4-1 UNI"},
    164: {"manufacturer": "Fronius", "model": "IG Plus V/A 10.0-1 UNI"},
    165: {"manufacturer": "Fronius", "model": "IG Plus V/A 7.5-1 UNI"},
    166: {"manufacturer": "Fronius", "model": "IG Plus V/A 6.0-1 UNI"},
    167: {"manufacturer": "Fronius", "model": "IG Plus V/A 5.0-1 UNI"},
    168: {"manufacturer": "Fronius", "model": "IG Plus V/A 3.8-1 UNI"},
    169: {"manufacturer": "Fronius", "model": "IG Plus V/A 3.0-1 UNI"},
    170: {"manufacturer": "Fronius", "model": "IG Plus 150 V-3"},
    171: {"manufacturer": "Fronius", "model": "IG Plus 120 V-3"},
    172: {"manufacturer": "Fronius", "model": "IG Plus 100 V-2"},
    173: {"manufacturer": "Fronius", "model": "IG Plus 100 V-1"},
    174: {"manufacturer": "Fronius", "model": "IG Plus 70 V-2"},
    175: {"manufacturer": "Fronius", "model": "IG Plus 70 V-1"},
    176: {"manufacturer": "Fronius", "model": "IG Plus 50 V-1"},
    177: {"manufacturer": "Fronius", "model": "IG Plus 35 V-1"},
    178: {"manufacturer": "SunPower", "model": "SPR 11400f-3 208/240"},
    179: {"manufacturer": "SunPower", "model": "SPR 12000f-277"},
    180: {"manufacturer": "SunPower", "model": "SPR 10000f"},
    181: {"manufacturer": "SunPower", "model": "SPR 10000F EU"},
    182: {"manufacturer": "Fronius", "model": "CL 33.3 Delta"},
    183: {"manufacturer": "Fronius", "model": "CL 44.4 Delta"},
    184: {"manufacturer": "Fronius", "model": "CL 55.5 Delta"},
    185: {"manufacturer": "Fronius", "model": "CL 36.0 WYE277"},
    186: {"manufacturer": "Fronius", "model": "CL 48.0 WYE277"},
    187: {"manufacturer": "Fronius", "model": "CL 60.0 WYE277"},
    188: {"manufacturer": "Fronius", "model": "CL 36.0"},
    189: {"manufacturer": "Fronius", "model": "CL 48.0"},
    190: {"manufacturer": "Fronius", "model": "IG TL 3.0"},
    191: {"manufacturer": "Fronius", "model": "IG TL 4.0"},
    192: {"manufacturer": "Fronius", "model": "IG TL 5.0"},
    193: {"manufacturer": "Fronius", "model": "IG TL 3.6"},
    194: {"manufacturer": "Fronius", "model": "IG TL Dummy"},
    195: {"manufacturer": "Fronius", "model": "IG TL 4.6"},
    196: {"manufacturer": "SunPower", "model": "SPR 12000F EU"},
    197: {"manufacturer": "SunPower", "model": "SPR 8000F EU"},
    198: {"manufacturer": "SunPower", "model": "SPR 6500F EU"},
    199: {"manufacturer": "SunPower", "model": "SPR 4000F EU"},
    200: {"manufacturer": "SunPower", "model": "SPR 3300F EU"},
    201: {"manufacturer": "Fronius", "model": "CL 60.0"},
    202: {"manufacturer": "SunPower", "model": "SPR 12000f"},
    203: {"manufacturer": "SunPower", "model": "SPR 8000f"},
    204: {"manufacturer": "SunPower", "model": "SPR 6500f"},
    205: {"manufacturer": "SunPower", "model": "SPR 4000f"},
    206: {"manufacturer": "SunPower", "model": "SPR 3300f"},
    207: {"manufacturer": "Fronius", "model": "IG Plus 12.0-3 WYE277"},
    208: {"manufacturer": "Fronius", "model": "IG Plus 50"},
    209: {"manufacturer": "Fronius", "model": "IG Plus 100"},
    210: {"manufacturer": "Fronius", "model": "IG Plus 100"},
    211: {"manufacturer": "Fronius", "model": "IG Plus 150"},
    212: {"manufacturer": "Fronius", "model": "IG Plus 35"},
    213: {"manufacturer": "Fronius", "model": "IG Plus 70"},
    214: {"manufacturer": "Fronius", "model": "IG Plus 70"},
    215: {"manufacturer": "Fronius", "model": "IG Plus 120"},
    216: {"manufacturer": "Fronius", "model": "IG Plus 3.0-1 UNI"},
    217: {"manufacturer": "Fronius", "model": "IG Plus 3.8-1 UNI"},
    218: {"manufacturer": "Fronius", "model": "IG Plus 5.0-1 UNI"},
    219: {"manufacturer": "Fronius", "model": "IG Plus 6.0-1 UNI"},
    220: {"manufacturer": "Fronius", "model": "IG Plus 7.5-1 UNI"},
    221: {"manufacturer": "Fronius", "model": "IG Plus 10.0-1 UNI"},
    222: {"manufacturer": "Fronius", "model": "IG Plus 11.4-1 UNI"},
    223: {"manufacturer": "Fronius", "model": "IG Plus 11.4-3 Delta"},
    224: {"manufacturer": "Fronius", "model": "Galvo 3.0-1"},
    225: {"manufacturer": "Fronius", "model": "Galvo 2.5-1"},
    226: {"manufacturer": "Fronius", "model": "Galvo 2.0-1"},
    227: {"manufacturer": "Fronius", "model": "IG 4500-LV"},
    228: {"manufacturer": "Fronius", "model": "Galvo 1.5-1"},
    229: {"manufacturer": "Fronius", "model": "IG 2500-LV"},
    230: {"manufacturer": "Fronius", "model": "Agilo 75.0-3"},
    231: {"manufacturer": "Fronius", "model": "Agilo 100.0-3 Dummy"},
    232: {"manufacturer": "Fronius", "model": "Symo 10.0-3-M"},
    233: {"manufacturer": "Fronius", "model": "Symo 12.5-3-M"},
    234: {"manufacturer": "Fronius", "model": "IG 5100"},
    235: {"manufacturer": "Fronius", "model": "IG 4000"},
    236: {"manufacturer": "Fronius", "model": "Symo 8.2-3-M Dummy"},
    237: {"manufacturer": "Fronius", "model": "IG 3000"},
    238: {"manufacturer": "Fronius", "model": "IG 2000"},
    239: {"manufacturer": "Fronius", "model": "Galvo 3.1-1 Dummy"},
    240: {"manufacturer": "Fronius", "model": "IG Plus 80 V-3"},
    241: {"manufacturer": "Fronius", "model": "IG Plus 60 V-3"},
    242: {"manufacturer": "Fronius", "model": "IG Plus 55 V-3"},
    243: {"manufacturer": "Fronius", "model": "IG 60 ADV"},
    244: {"manufacturer": "Fronius", "model": "IG 500"},
    245: {"manufacturer": "Fronius", "model": "IG 400"},
    246: {"manufacturer": "Fronius", "model": "IG 300"},
    247: {"manufacturer": "Fronius", "model": "Symo 3.0-3-S"},
    248: {"manufacturer": "Fronius", "model": "Galvo 3.1-1"},
    249: {"manufacturer": "Fronius", "model": "IG 60 HV"},
    250: {"manufacturer": "Fronius", "model": "IG 40"},
    251: {"manufacturer": "Fronius", "model": "IG 30 Dummy"},
    252: {"manufacturer": "Fronius", "model": "IG 30"},
    253: {"manufacturer": "Fronius", "model": "IG 20"},
    254: {"manufacturer": "Fronius", "model": "IG 15"},
}
