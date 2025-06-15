from types import SimpleNamespace

def load_config(config_path=None):
    """
    Proje yapılandırmasını yükler ve bir SimpleNamespace nesnesi olarak döndürür.
    """
    config = SimpleNamespace(
        preprocessing=SimpleNamespace(
            lower_case=True,
            remove_punctuation=False
        ),
        features=SimpleNamespace(
            window_size=2,
            use_morphological=True
        ),
        model=SimpleNamespace(
            algorithm='lbfgs',
            c1=0.1,
            c2=0.1,
            max_iterations=100
        ),
        monitoring=SimpleNamespace(
            log_performance=True
        ),
        paths=SimpleNamespace(
            data_dir='../data/',
            model_save_path='../models/pos_tagger.pkl'
        )
    )
    return config