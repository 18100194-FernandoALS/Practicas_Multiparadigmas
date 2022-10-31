import logging as log
log.basicConfig(level=log.DEBUG,    #El level son 5, debug, information, , , critico. En otros es mejor usar warning
                format="%(asctime)s: %(levelname)s [%(filename)s]: %(lineno)s %(message)s",
                datefmt='%I:%M:%S %p',
                handlers = [
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])


if __name__ == '__main__': #si solo quiero probar un archivo, solo se ejecute esa parte, no aparecera esto ya que esta fuera del archivo
    log.debug("Mensaje Debug")