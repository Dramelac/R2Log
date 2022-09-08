import R2Log


def test_logger_levels():
    R2Log.logger.setLevel("VERBOSE")
    assert R2Log.logger.getEffectiveLevel() == R2Log.R2Log.VERBOSE
    R2Log.logger.setLevel(R2Log.R2Log.SUCCESS)
    assert R2Log.logger.getEffectiveLevel() == R2Log.R2Log.SUCCESS
    R2Log.logger.setLevel("ADVANCED")
    assert R2Log.logger.getEffectiveLevel() == R2Log.R2Log.ADVANCED
