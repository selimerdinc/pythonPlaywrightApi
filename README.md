## Giriş
> API testlerinde, gerçek sunucuya yapılan çağrılar bazen istenmeyen yan etkilere sebep olabilir. Testlerimizin güvenilirliğini artırmak ve bağımlılıkları azaltmak için, API çağrılarını mocklamak (sahte yanıtlar oluşturmak) yaygın bir yaklaşımdır. Bu makalede, Playwright kullanarak API çağrılarını nasıl mocklayabileceğimizi ele alacağız.

## Kurulum
```bash
pip install -r requirements.txt
```

## Playwright Kurulumu
- Playwright'i yüklemek için aşağıdaki komutu çalıştırın:
```bash
- playwright install
```

## Kullanım
```bash
python -m pytest UserApi/tests/GetUser.py
```
