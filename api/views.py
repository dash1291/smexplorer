from django.http import HttpResponse

from api.helpers import encode_xml, encode_json
from explorer.models import Directory, File

class ApiBase(object):

	def __call__(self, request, *args, **kwargs):
		self.format = request.REQUEST.get('format')
		self.mimetype = ('text/xml' if self.format == 'xml ' else 'application/json')
		self.process_request(*args, **kwargs)

 	def build_response(self, response_array):
 		if self.format == 'xml':
 			response_str = self.encode_xml(response_array)
 		else:
 			response_str = self.encode_json(response_array)
 	
 		response_str = self.encode_response()
 		return response_str

 	def render(self, response_array):
 		return HttpResponse(self.build_response(response_array))


class DataApi(ApiBase):
	def process_request(self, *args, **kwargs):
		if object_type == 'folder':
			if action == 'list':
				self.list_directory(uid)

	def list_directory(self, file_path):
		files = File.objects.filter(path=file_path)
		files_array = []
		for file in files:
			files_array.append({'name': file.name})

		return self.render({'files': files_array})