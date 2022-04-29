from rest_framework import serializers


from .models import ExperimentRepo#,Experimentcount
from .models import SuccessMetric
from .models import GroupDetails, Factor, Levels, Constraints, ScopeFilters

class ExperimentRepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentRepo
        fields = ["experimentId", "experimentName", "numberOfGroups","hypothesis","isCostAssociated",
        "measurementStartDate","measurementEndDate","testStartDate","testEndDate","referenceEndDate","referenceStartDate","hypothesis","marketMasterId","spacialGranularityMasterId","productGranularityMasterId"]

'''
class ExperimentcountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experimentcount
        fields = ["exprepoid"]
'''
class ExperimentCountSerializer(serializers.ModelSerializer):
    user_count = serializers.SerializerMethodField()

    class Meta:
        model = ExperimentRepo
        fields = ( 'user_count')   

    def get_user_count(self, obj):
        return ExperimentRepo.objects.all().count()        

class SuccessMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessMetric
        fields = ["successMetricId"]

class GroupDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupDetails
        fields = ["groupDetailsId","groupName","groupDescription","costPerExperiment","percentageAllocation","isControlGroup"]

class FactorSerializer(serializers.ModelSerializer):
    class Meta:
       model = Factor
       fields = ["factorId"]

class LevelsSerializer(serializers.ModelSerializer):
    class Meta:
       model = Levels
       fields = ["levelId"]

class ConstraintsSerializer(serializers.ModelSerializer):
    class Meta:
       model = Constraints
       fields = ["constraintId"]

class ScopeFiltersSerializer(serializers.ModelSerializer):
    class Meta:
       model = ScopeFilters
       fields = ["scopeFilterId"]

#The ListSerializer class provides the behavior for serializing and validating multiple objects at once.
class BulkCreateUpdateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):

        result = [self.child.create(attrs) for attrs in validated_data]

        try:
            self.child.Meta.model.objects.bulk_create(result)
        except IntegrityError as e:
            raise ValidationError(e)

        update_project_last_modified(result)

        return result