from vjmagic import constants
from vjmagic.config.hypnodrome_alpha import config as hypnodrome_alpha
from vjmagic.config.hypnodrome_beta import config as hypnodrome_beta
from vjmagic.config.hypnodrome_gamma import config as hypnodrome_gamma
from vjmagic.config.hypnotouch import config as hypnotouch_config

bankmap = [
    {
        'key': constants.HYPNO_ALPHA,
        'title': 'HYPNO ALPHA',
        'config': hypnodrome_alpha,
    },
    {
        'key': constants.HYPNO_BETA,
        'title': 'HYPNO BETA',
        'config': hypnodrome_beta,
    },
    {
        'key': constants.HYPNO_GAMMA,
        'title': 'HYPNO GAMMA',
        'config': hypnodrome_gamma,
    },
    {
        'key': constants.HYPNO_ADV,
        'title': 'ADVANCED: touch-knob effects, speed-warp video',
        'config': hypnotouch_config,
    },
]
