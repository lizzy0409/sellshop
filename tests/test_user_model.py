from user.models import Profile


def test_object_is_instance_of_model(db, user_obj):
    assert isinstance(user_obj, Profile)
