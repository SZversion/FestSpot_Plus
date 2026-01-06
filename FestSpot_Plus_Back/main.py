import uvicorn
from core import config


def main():
    uvicorn.run(app=config.APP, host=config.HOST, port=config.PORT, reload=True)


if __name__ == "__main__":
    main()
