# from app.core.config import get_settings
#
#
# def test_settings_load_from_env(monkeypatch):
#     # Set environment variables temporarily
#     monkeypatch.setenv("POSTGRES_HOST", "localhost")
#     monkeypatch.setenv("POSTGRES_PORT", "5432")
#     monkeypatch.setenv("POSTGRES_USER", "anderdam")
#     monkeypatch.setenv("POSTGRES_PASSWORD", "test")
#     monkeypatch.setenv("POSTGRES_DB", "tracker")
#     monkeypatch.setenv("SECRET_KEY", "testkey")
#
#     settings = get_settings()
#
#     assert settings.postgres_host == "localhost"
#     assert settings.postgres_port == 5432
#     assert settings.postgres_user == "anderdam"
#     assert settings.postgres_password == "test"
#     assert settings.postgres_db == "tracker"
#     assert settings.attachments_dir == "/data/attachments"
#     assert settings.database_url == "postgresql://anderdam:test@localhost:5432/tracker"
