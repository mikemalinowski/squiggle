

#Overview

Squiggle is a mechanism for storing dictionary data within a multitude
of different host environments (for a specific list please look at the
hosts directory).

Squiggle will automatically return the correct dictionary type for your
given host, from which point you can update/edit the dictionary and then
ask for that dictionary to be saved. 

That dictionary will then be stored persistently within the scene/context.

The following example shows how to create a new dictionary:

```python
    
    # -- Import squiggle
    import squiggle
    
    # -- Create a dictionary to store information with
    data = squiggle.get('foobar')
    
    # -- Update some data in the ditionary
    data['bing'] = 'bong'
    
    # -- Calling save will trigger the dictionary to be stored
    # -- in the scene persistently.
    data.save()
```

You can then access the dictionary in exactly the same way, for 
instance:

```python

    # -- Import squiggle
    import squiggle
    
    # -- Create a dictionary to store information with
    data = squiggle.get('foobar')
    
    print(data)
    # {'bing': 'bong'}
```

Note: All data stored using squiggle must be json serialisable.
