from django.contrib.auth.models import Group, User
from rest_framework import serializers

# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #
# ///// # ///// # TITULAR: Tutorial quickstart
# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

"""

- Explicacion:

- que son los serializadores & deserializadores:
    - Los serializadores son clases que convierte las instancias de un objeto en formato json.
    - los deserializadores son clases que obtienen el arreglo de un json para convertirlo en la instancia de un objeto.
    - los serializadores tambien pueden hacer validacion de datos.
    - Especificar o personzalizar los serializadores puede tener mayores beneficios en la mayoria de los casos complejos.
    
- para que sirven:
    - facilitan las APIREST al serializaar y des-serializar de forma eficiente.

"""

# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #
# ///// # ///// # TITULAR: Tutorial quickstart
# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #
