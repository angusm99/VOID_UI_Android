"""
Regenerate all 108 placeholder Terminal icons as WHITE monoline glyphs,
reusing the shared generator (glyph dict + core-glyph matching) from
generate_xeno_mono. Terminal sources were 105/108 byte-identical placeholders.
"""
import generate_xeno_mono as g

if __name__ == "__main__":
    g.main(prefix="terminal_", master_dir=g.MASTER_TERMINAL)
