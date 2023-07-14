"""Top-level package for BioGTR."""
from __future__ import absolute_import

from . import (
    datasets,
    inference,
    models,
    training,
)

from biogtr.version import __version__
from biogtr.models.attention_head import MLP, ATTWeightHead
from biogtr.models.visual_encoder import VisualEncoder
from biogtr.models.embedding import Embedding
from biogtr.models.transformer import Transformer
