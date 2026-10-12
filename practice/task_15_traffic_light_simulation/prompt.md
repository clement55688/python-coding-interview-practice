# Module 15: Two-direction traffic light simulation

Original practice exercise inspired by a [publicly shared candidate experience from June 2025](https://www.jointaro.com/interviews/companies/benchling/experiences/software-engineer-united-states-june-20-2025-no-offer-positive-d21a4960/). This is not a verified or actual Benchling interview question.

Implement `simulate_traffic(timings, ticks)`. `timings` has entries for `"EW"` and `"NS"`, each containing positive integer durations for `"green"`, `"yellow"`, and `"red"`. `ticks` is a non-negative integer.

The controller starts with East-West green and North-South red. Repeat this sequence:

1. EW green for `timings["EW"]["green"]` ticks; NS stays red.
2. EW yellow for `timings["EW"]["yellow"]` ticks; NS stays red.
3. Both directions red for `timings["EW"]["red"]` ticks.
4. NS green for `timings["NS"]["green"]` ticks; EW stays red.
5. NS yellow for `timings["NS"]["yellow"]` ticks; EW stays red.
6. Both directions red for `timings["NS"]["red"]` ticks.

Return a list of `(ew_color, ns_color)` pairs, one for each tick. Record the state at the start of each tick; after the final requested tick, do not include an extra state. For zero ticks, return an empty list.

Raise `ValueError` unless the timing configuration has exactly the two directions and three required colors, each duration is a positive integer (booleans are not valid integers here), and `ticks` is a non-negative integer (also excluding booleans). Do not mutate the input.

Example: with EW timings `green=2, yellow=1, red=1`, NS timings `green=1, yellow=1, red=1`, and `ticks=5`, return:

```python
[
    ("GREEN", "RED"),
    ("GREEN", "RED"),
    ("YELLOW", "RED"),
    ("RED", "RED"),
    ("RED", "GREEN"),
]
```

Before coding, clarify the tick convention and explain how you will avoid stepping through time after all requested output has been produced. State the time and space complexity.
