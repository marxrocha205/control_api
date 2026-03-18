from apscheduler.schedulers.background import BackgroundScheduler

from app.services.cron import rodar_automacao

scheduler = BackgroundScheduler()


def iniciar_scheduler():
    """
    Agenda execução diária
    """

    scheduler.add_job(rodar_automacao, "interval", hours=24)

    scheduler.start()