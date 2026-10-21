# Release Checklist

A release publishes the method under a version number. Publication is irreversible in practice: PDFs are downloaded, cited and evaluated against. No release happens without the maintainer's explicit approval.

## Before the release

1. **Open decisions.** Every open decision (`docs/open-decisions.md`) that the release text depends on is resolved, or the release text keeps it explicitly labeled as proposed.
2. **Version.** Choose the number according to the versioning policy (OD-11): MAJOR if an obligation can turn an earlier *satisfied* or *not applicable* outcome into *violated*; MINOR for clarifications and new non-normative material; PATCH for editorial changes. Update `manifest.yaml` (no `-draft` suffix).
3. **Change log.** `CHANGELOG.md` has an entry for the version. Each item is classified as normative, clarifying or editorial, and every normative change is listed.
4. **Bilingual parity.** `make check` passes. Read the changed passages in both languages: the check verifies structure and formulas, not meaning.
5. **Build.** The CI build of the release commit is green. Download the PDF artifact and inspect both PDFs: cover version, table of contents, formulas, diagrams, glossary, references.
6. **Review.** The pull request with the release content has been reviewed and merged by the maintainer.

## Publishing

7. Tag the merged commit: `git tag -a v<version> -m "ESEM <version>"` and `git push origin v<version>`.
8. CI verifies that the tag matches `manifest.yaml`, builds the PDFs in the Docker toolchain and publishes the GitHub release with both PDFs.
9. Alternatively, run the workflow manually with `release: true`. It publishes the manifest version from the selected commit.

## After publishing

10. Check that the release has both PDFs and that their cover shows the right version.
11. Set `manifest.yaml` to the next `-draft` version on `master`.

## Reproducing a published build

```sh
git checkout v<version>
make docker-pdf      # uses the commit time of HEAD as SOURCE_DATE_EPOCH
```

The resulting PDFs have the same text and layout as the published ones. They are not guaranteed to be byte-identical: the cover is rendered by `wkhtmltopdf`, which embeds its own creation metadata.
