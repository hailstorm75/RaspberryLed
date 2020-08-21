def nameof(obj):
  return getattr(obj, '__name__', type(obj))
