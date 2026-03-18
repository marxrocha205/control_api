# Esse arquivo executa a automação

from app.database import SessionLocal
from app.services.assinatura_service import (
    atualizar_status_assinaturas,
    buscar_vencendo_hoje
)
from app.services.whatsapp_service import enviar_whatsapp


def rodar_automacao():
    """
    Executa rotina diária
    """

    db = SessionLocal()

    try:
        # 1️⃣ Atualiza status
        atualizar_status_assinaturas(db)

        # 2️⃣ Busca quem vence hoje
        assinaturas = buscar_vencendo_hoje(db)

        for assinatura in assinaturas:

            cliente = assinatura.cliente

            mensagem = (
                f"Olá {cliente.nome}, seu plano vence hoje! "
                "Renove para continuar usando."
            )

            enviar_whatsapp(cliente.telefone, mensagem)

    finally:
        db.close()