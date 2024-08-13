toc_entries = [
    (1, 150, 12345),
    (151, 300, 23456),
    (301, 450, 34567),
    # ... more TOC entries
]

musicbrainz_disc_id = generate_musicbrainz_disc_id(toc_entries)
print(musicbrainz_disc_id)
