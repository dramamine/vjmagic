from vjmagic import constants
from vjmagic.config.hypnodrome import config as hypno_new_config
from vjmagic.config.hypnotouch import config as hypnotouch_config

bankmap = [
    {
        'key': constants.HYPNO_ALPHA,
        'title': 'HYPNO ALPHA',
        'config': hypno_new_config,
    },
    {
        'key': constants.HYPNO_BETA,
        'title': 'HYPNO BETA',
        'config': hypno_new_config,
    },
    {
        'key': constants.HYPNO_GAMMA,
        'title': 'HYPNO GAMMA',
        'config': hypno_new_config,
    },
    {
        'key': constants.HYPNO_ADV,
        'title': 'ADVANCED: touch-knob effects, speed-warp video',
        'config': hypnotouch_config,
    },
]
