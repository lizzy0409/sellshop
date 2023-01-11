from core.models import Creative_team, Contact


def test_creative_team_object_is_instance_of_model(db, creative_team_obj):
    assert isinstance(creative_team_obj, Creative_team)


def test_contact_object_is_instance_of_model(db, contact_obj):
    assert isinstance(contact_obj, Contact)