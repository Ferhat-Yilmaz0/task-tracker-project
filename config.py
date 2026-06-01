import os


class Config:
    """Tüm ortamlar için ortak temel ayarlar."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """Geliştirme ortamı ayarları."""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///dev.db"
    )


class ProductionConfig(Config):
    """Production ortamı ayarları."""

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///prod.db"
    )

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        # Production'a özgü başlatma işlemleri buraya eklenebilir.


class TestingConfig(Config):
    """Test ortamı ayarları."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    WTF_CSRF_ENABLED = False


# Factory fonksiyonunda config_name ile seçmek için kullanılır.
config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig,
}
