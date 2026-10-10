# BlackKnight chrome on Sci-Fi

First slice: window title/border and shelf artwork; keep original EDC programs and geometry. See [material concept](../../../docs/blue-steel-pass.md).

Editable base discovered at the local path recorded in asset-contract.json. Its correspondence to the installed EDJ and its author/license still require verification. No upstream files are vendored here.

The asset contract records original PNG dimensions and hashes. Author original replacement plates and glints into overrides/wrk at those exact dimensions. Nine original replacement PNGs are now present, with editable SVGs in sources/ and hashes in artwork-provenance.json. They are first dimensioned candidates; target rendering is still pending.

Remote build invocation: `sh build.sh /staged/editable-scifi /outputs/new-run`. Supply an approved EFL compiler via the BKC toolchain. This stages a separate tree and outputs blackknight-scifi.edj; it does not install or select a desktop theme. Keep output outside tracked source. No compiler or runtime validation has occurred.
