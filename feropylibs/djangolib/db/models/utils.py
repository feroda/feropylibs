from django.db.models import Manager

def reklass_model(model_instance, model_subklass):
    """
    Create an instance of model_subklass given a model_instance.
    """

    # KO OLD: fields = model_instance._meta.get_all_field_names()
    # Django 1.9
    fields = [f.name for f in model_instance._meta.get_fields()]
    kwargs = {}
    for field_name in fields:
        try:
            kwargs[field_name] = getattr(model_instance, field_name)
            if isinstance(kwargs[field_name], Manager):
                # This is a ManyToMany reversed field, not-so-safe pra
                del kwargs[field_name]
        except AttributeError as e:
            # needed for Related models for not already saved instances
            pass
        except ValueError as e:
            # needed for ManyToManyField for not already saved instances
            pass

    return model_subklass(**kwargs)
