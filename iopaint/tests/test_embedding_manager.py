# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# from functools import partial
# from iopaint.model.anytext.ldm.modules.diffusionmodules.util import conv_nd, linear
# from iopaint.model.anytext.cldm.embedding_manager import EmbeddingManager, coverage_tracker

# import pytest
# from unittest.mock import MagicMock

# @pytest.fixture
# def setup_embedding_manager():
#     embedder = MagicMock()
#     embedder.tokenizer = MagicMock()
#     embedder.vit = MagicMock()
#     embedder.processor = MagicMock()
#     return EmbeddingManager(embedder, emb_type='vit', add_pos=True)

# def test_init_with_vit_and_position(setup_embedding_manager):
#     assert coverage_tracker['init_emb_type_vit']
#     assert coverage_tracker['init_add_pos']

# def test_encode_text_no_lines(setup_embedding_manager):
#     text_info = {'n_lines': [], 'gly_line': [], 'positions': []}
#     setup_embedding_manager.encode_text(text_info)
#     assert coverage_tracker['encode_no_lines'] == False  # Expecting no lines processed
