build:
	maturin develop --release

test_chunk:
	pytest.exe qvd\test_qvd_reader_chunk.py -rx -rP