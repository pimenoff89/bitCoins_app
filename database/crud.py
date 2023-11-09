import datetime
import config
import pydantic_models
import models
import bit

wallet = bit.PrivateKeyTestnet(config.testnet_wallet)  # наш кошелек готов и содержится в переменной wallet
print(f"Баланс: {wallet.get_balance()}")
print(f"Адрес: {wallet.address}")
print(f"Приватный ключ: {wallet.to_wif()}")

wallet.get_transactions()
transaction = wallet.send(outputs)
print(transaction)