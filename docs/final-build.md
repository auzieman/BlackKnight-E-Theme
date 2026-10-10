# Final BlackKnight local build

Accepted source: `ec07f89`. BKC run: `1e17f03e-a97b-4b43-a027-2375afdf2cfc`. Immutable payload SHA256: `c770e4610e0322ef0f82f7517f73280a76b6576b4807a9bbc9417df5c37526df`.

Final package: `build/out/BlackKnight-final-ec07f89/`, with archive `build/out/BlackKnight-final-ec07f89.tar.gz`. It contains:

- `BlackKnight-BlueSteel.edj`: accepted blue-steel window/shelf artwork and AuzieTek griffin emblem.
- `BlackKnight-Storm.edj`: production wallpaper with 90-second distant cloud drift and approximately 53-second moon-cover/dim/strike/clear sequence.
- `BlackKnight-Still.edj`: static alternative.
- `BlackKnight Ice.eet`: optional terminal palette candidate.
- Manifest, checksums, image remap verification, artwork provenance and installed compiler-package inventory.

All seven compiler artifact checksums passed. The theme archive verification confirms 64 image-only replacements and 4,595 byte-identical unchanged entries. Existing donor EDC layouts, programs and interaction contracts remain intact. Final output logs and binaries are retained under `build/out/blackknight-final/`.

The local theme/wallpaper candidate files were refreshed using `install-local.sh`. Current desktop selections remain unchanged. Select **BlackKnight-BlueSteel** in Enlightenment theme settings and **BlackKnight-Storm** in wallpaper settings when ready; the previous 20-second automatically restored trial remains documented in setup-test.md. The final production wallpaper completed cover, strike and clear/reset in the native preview; monotonic phase timestamps are recorded in docs/task.md. Terminal palette visual acceptance and idle performance checks remain follow-ups.

Repackage a verified artifact directory with `themes/blackknight/desktop/package-final.py ARTIFACT_DIRECTORY OUTPUT_DIRECTORY --run-id RUN_ID --payload-sha256 SHA256`. This final local build is not a public/tagged release.
