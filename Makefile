build:
	maturin develop --release

test:
	pytest.exe qvd\test_qvd_reader.py -rx -rP

test_chunk:
	pytest.exe qvd\test_qvd_reader_chunk.py -rx -rP
