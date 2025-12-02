from src.backup_configs import load_inventory

def test_load_inventory(tmp_path):
    data = """---
hosts:
  r1:
    hostname: 1.1.1.1
"""
    p = tmp_path / "hosts.yaml"
    p.write_text(data)
    inv = load_inventory(str(p))
    assert 'hosts' in inv
    assert 'r1' in inv['hosts']
