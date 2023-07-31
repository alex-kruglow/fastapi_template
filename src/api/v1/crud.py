"""CRUD api/v1/crud module."""

from logging import getLogger

from fastapi import APIRouter, Depends

from models.event import Event
from models.mass_mailing import MassMailing

from services.notification_service import (
    NotificationService, get_notification_service
)


router: APIRouter = APIRouter()

logger = getLogger()


@router.get('/')
async def get_item():
    pass


@router.post('/new')
async def new_item():
    pass


@router.put('/update')
async def update_item():
    pass


@router.delete('/delete')
async def delete_item():
    pass