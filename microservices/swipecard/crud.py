import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from sqlalchemy.orm import Session
from swipecard.models.mr_liked_hated_member import MR_Liked_Hated_Member
from swipecard.models.mr_member import MR_Member
from swipecard.models.mr_member_tag import MR_Member_Tag
from swipecard.models.user import User
from swipecard.schemas import SwipeCardPreference


class CRUDSwipeCard:
    def save_preference(
        self, db: Session, *, obj_in: SwipeCardPreference
    ) -> MR_Liked_Hated_Member:
        db_obj = MR_Liked_Hated_Member(
            member_id=obj_in.member_id,
            target_member_id=obj_in.target_member_id,
            room_uuid=obj_in.room_uuid,
            is_liked=obj_in.is_liked,
            is_hated=obj_in.is_hated,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_preference_by_member_id_and_room_uuid(
        self, db: Session, *, member_id: str, room_uuid: str
    ) -> MR_Liked_Hated_Member:
        return (
            db.query(MR_Liked_Hated_Member)
            .filter(
                MR_Liked_Hated_Member.member_id == member_id,
                MR_Liked_Hated_Member.room_uuid == room_uuid,
            )
            .all()
        )

    def get_mr_member_by_room_uuid(self, db: Session, *, room_uuid: str) -> MR_Member:
        return db.query(MR_Member).filter(MR_Member.room_uuid == room_uuid).all()

    def get_self_tag_by_member_id_and_room_uuid(
        self, db: Session, *, member_id: str, room_uuid: str
    ) -> MR_Member_Tag:
        return (
            db.query(MR_Member_Tag)
            .filter(
                MR_Member_Tag.member_id == member_id,
                MR_Member_Tag.room_uuid == room_uuid,
                MR_Member_Tag.is_self_tag == True,
                MR_Member_Tag.is_find_tag == False,
            )
            .all()
        )

    def get_find_tag_by_member_id_and_room_uuid(
        self, db: Session, *, member_id: str, room_uuid: str
    ) -> MR_Member_Tag:
        return (
            db.query(MR_Member_Tag)
            .filter(
                MR_Member_Tag.member_id == member_id,
                MR_Member_Tag.room_uuid == room_uuid,
                MR_Member_Tag.is_self_tag == False,
                MR_Member_Tag.is_find_tag == True,
            )
            .all()
        )

    def get_user_profile_by_member_id(self, db: Session, *, member_id: str) -> User:
        mr_member = db.query(MR_Member).filter(MR_Member.member_id == member_id).first()
        user_uuid = mr_member.user_uuid
        return db.query(User).filter(User.user_uuid == user_uuid).first()

    # def create(self, db: Session, *, obj_in: SwipeCardCreate) -> SwipeCard:
    #     db_obj = SwipeCard(

    #     )
    #     db.add(db_obj)
    #     db.commit()
    #     db.refresh(db_obj)
    #     return db_obj

    # def delete(self, db: Session, *, db_obj: SwipeCard):
    #     return True


swipe_card = CRUDSwipeCard()
