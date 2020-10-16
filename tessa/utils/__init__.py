# Using try except to give to not get a error while building wheel without reconplogger
try:
    import reconplogger
    logger = reconplogger.logger_setup()

except ImportError:
    print("*********reconplogger missing********")