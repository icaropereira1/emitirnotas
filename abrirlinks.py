from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os
from dotenv import load_dotenv

load_dotenv()

def abrir_relatorios_e_clicar_botoes(instancia, mes, ano, primeiro_dia, ultimo_dia):
    print(f"Iniciando a automação de emissão de notas para a instância: '{instancia}' para a data {primeiro_dia}/{mes}/{ano} até a data {ultimo_dia}/{mes}/{ano}")

    # --- Configuração do WebDriver ---
    service = Service()
    
    try:
        driver = webdriver.Chrome(service=service)
    except Exception as e:
        print(f"ERRO: Não foi possível iniciar o navegador. Verifique sua instalação do Chrome e do Python/Selenium.")
        print(f"Erro original: {e}")
        return

    # URL base para a qual o script irá navegar
    url_base = f"https://{instancia}.vucasolution.com.br/retaguarda/pg_financeiro_fiscal_nfce_delivery.php?csv=0&datahora_inicio={{:02d}}%2F{mes:02d}%2F{ano}+00%3A00&datahora_fim={{:02d}}%2F{mes:02d}%2F{ano}+23%3A59&data_tipo=data&id_canal=&id_formapagamento=&id_status=aguardando&nfce="
    
    # --- Loop de Navegação e Automação ---
    for dia in range(primeiro_dia, ultimo_dia + 1):
        url_completa = url_base.format(dia, dia)
        
        print(f"Navegando para o dia {dia:02d}...")

        driver.execute_script("window.open('');")
        
        time.sleep(2)
        
        driver.switch_to.window(driver.window_handles[-1])
        
        driver.get(url_completa)
        
        # --- Lógica do Atraso para o Login ---
        if dia == 1:
            time.sleep(2)
            botao_nao_autenticado = driver.find_element(By.CLASS_NAME, "confirm")
            botao_nao_autenticado.click()
            
            print("Fazer o login...")
            
            checkbox_login = driver.find_element(By.NAME, "auth_login")
            checkbox_login.click()
            checkbox_login.send_keys(os.getenv("login"))

            senha_login = driver.find_element(By.NAME, "auth_senha")
            senha_login.click()
            senha_login.send_keys(os.getenv("senha"))

            botao_login = driver.find_element(By.CLASS_NAME, "btn-login")     
            botao_login.click()

            time.sleep(3)

        else:
            time.sleep(3) 

        try:
            # Encontrar e clicar no checkbox "js-all"
            checkbox_todos = driver.find_element(By.CLASS_NAME, "js-all")
            checkbox_todos.click()
            print(f" -> Checkbox 'js-all' clicado com sucesso para o dia {dia:02d}!")

            time.sleep(1) 
            # Encontrar e clicar no botão "Emitir NFCe"
            botao_emitir = driver.find_element(By.CLASS_NAME, "js-emitirNFCE")
            botao_emitir.click()
            print(f" -> Botão 'Emitir NFCe' clicado com sucesso!")

        except Exception as e:
            print(f" -> ERRO: Não foi possível encontrar ou clicar nos botões para o dia {dia:02d}. Erro: {e}")
            
        time.sleep(1)

    print("\nProcesso de automação concluído.")
    input("Pressione ENTER para fechar o navegador...")
    driver.quit()

# --- Configurações que você precisa modificar ---
if __name__ == "__main__":
    
    nome_da_instancia = 'urbanossmashburg' 
    mes_do_relatorio = 12
    ano_do_relatorio = 2025      
    primeirodia = 1
    ultimodia = 22

    abrir_relatorios_e_clicar_botoes(nome_da_instancia, mes_do_relatorio, ano_do_relatorio, primeirodia, ultimodia)