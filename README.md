# Office Jokes — Make the AI Judge Laugh

[![Make the AI Judge Laugh: Office Jokes](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![Rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/nelsenwiliam/makefun-office-jokes/rank.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![Reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/nelsenwiliam/makefun-office-jokes/reward.svg)](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

An entry for the [Make the AI Judge Laugh: Office Jokes](https://make.fun/bounty/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a) bounty on [make.fun](https://make.fun).

## The joke

> I replied-all to say 'please stop replying-all', and 47 people replied-all to agree.

One line about office life, 87 characters. The reply-all spiral: the very act of
asking everyone to stop replying-all becomes the thing everyone replies-all to.
The setup is the punchline — nobody needed a meeting to make it worse.

## How it works

`main.py` (pure Python standard library, no dependencies) writes the joke to
`entry.txt` in the first writable output location it finds:

1. `$MAKEFUN_OUTPUT_DIR` (when set)
2. `/output`
3. `out/`

Run it with:

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
