# Contributing

Thanks for your help. This project is a data pipeline plus a build step. Please change the pipeline, not the output.

## Do not edit generated files

These files are build output. A pull request that edits them by hand will be closed.

- `data/settings-urls.json`
- `docs/settings-urls.md`
- `shortcuts/**/*.shortcut`

Change a script, then rebuild.

## Set up

You need macOS and Python 3.9 or later. The `shortcuts` command comes with macOS 12 and later.

```sh
make fetch      # download the upstream sources into raw/
make all        # merge, write the docs, build the shortcuts, verify
make sign       # sign the shortcuts
```

## Add a URL

Most URLs come from an upstream source, not from this repository.

1. If the URL is in a new public list, add that list to `SOURCES` in `scripts/fetch_sources.py`, then add a parser in `scripts/merge.py`.
2. If the URL is only yours, say how you tested it, and on which iOS version. Put it in `overrides` style code in `scripts/merge.py` with a comment.

Always say which device and which iOS version you tested.

## Add a language

1. Add an entry to `LANGUAGES` in `scripts/build_shortcut.py`.
2. Apple ships labels for many languages. `scripts/merge.py` reads the `zh_TW` export today. To add another, copy the `ZH_FILES` block and the `label_zh` field.
3. Run `make shortcuts` and `make verify`.

## Before you open a pull request

1. Run `make verify`. It must print `ALL OK`.
2. Run `shellcheck scripts/sign_all.sh` if you changed that script.
3. Keep the commit message in Conventional Commits form, for example `feat(data): add iOS 26.3 export`.
