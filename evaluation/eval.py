#!/usr/bin/env python

from duckietown_challenges import wrap_evaluator, ChallengeEvaluator, ChallengeInterfaceEvaluator

import os

class Evaluator(ChallengeEvaluator):

    def prepare(self, cie):
        cie.set_challenge_parameters({'dummy': 1})

    def score(self, cie):
        solution_output = cie.get_solution_output_dict()

        guess = solution_output['guess']

        if not 0 <= guess <= 100:
            msg = 'Invalid score: should be between 0 and 100, got %s.' % guess
            raise InvalidSubmission(msg)
        elif guess == 51:
            score = 15
        else:
            score = 10

        cie.set_score('score1', score, 'How close it is to the magic number.')


if __name__ == '__main__':
    wrap_evaluator(Evaluator())
