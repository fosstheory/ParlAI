#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import random
from parlai.core.opt import Opt
from parlai.core.message import Message
from parlai.core.mutators import register_mutator, ExampleMutator


@register_mutator("word_reverse")
class WordReverseMutator(ExampleMutator):
    """
    Shuffles all the words in an example (text field).
    """

    def __init__(self, opt: Opt):
        super().__init__(opt)
        self.rng = random.Random(42)

    def example_mutation(self, message: Message) -> Message:
        texts = message.pop('text').split('\n')
        output_texts = []
        for text in texts:
            words = text.split(' ')
            words = list(reversed(words))
            output_texts.append(' '.join(words))
        message['text'] = '\n'.join(output_texts)
        return message