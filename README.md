# cron-action

```commandline
# example usagefor Python
jobs:
  cron:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: ./.github/actions/find_ongoing_feature_flags
        with:
          matcher: "is_upcoming_features_enabled\\('ENG-[0-9]{0,6}'\\)"
          identifier_matcher: "ENG-\\d{0,6}"
          file_type: "py"
          cutoff_in_days: "20"
```