from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'materialType', 'modules.registry.views.registry_checkboxes_materialType', name='Registry materialType Checkboxes'),
    url(r'structuralMorphology', 'modules.registry.views.registry_checkboxes_structuralMorphology', name='Registry structuralMorphology Checkboxes'),
    url(r'propertyClass', 'modules.registry.views.registry_checkboxes_propertyClass', name='Registry propertyClass Checkboxes'),
    url(r'experimentalDataAcquisitionMethod', 'modules.registry.views.registry_checkboxes_expAcquisitionMethod', name='Registry experimentalDataAcquisitionMethod Checkboxes'),
    url(r'computationalDataAcquisitionMethod', 'modules.registry.views.registry_checkboxes_compAcquisitionMethod', name='Registry computationalDataAcquisitionMethod Checkboxes'),
    url(r'sampleProcessing', 'modules.registry.views.registry_checkboxes_sampleProcessing', name='Registry sampleProcessing Checkboxes'),
    url(r'relevant-date', 'modules.registry.views.relevant_date', name='Relevant Date'),
    url(r'name-pid', 'modules.registry.views.name_pid', name='Name PID'),
    url(r'status', 'modules.registry.views.status', name='Status'),
    url(r'local-id', 'modules.registry.views.localid', name='Local ID'),
    url(r'description', 'modules.registry.views.description', name='Description'),
    url(r'resource-type', 'modules.registry.views.resource_type', name='Resource Type'),
)

