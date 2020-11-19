classdef ScarletClient
    properties
        serverIP
    end
    methods
        function obj = ScarletClient(serverIP)
            obj.serverIP = serverIP + ':8080/'
        end

        function uploadFile(obj,localFilePath, serverFilePath)
            data = fileread(localFilePath);
            contentTypeField = matlab.net.http.field.ContentTypeField('image/png'); %'image/jpeg'

            body = matlab.net.http.MessageBody(data);

            type1 = matlab.net.http.MediaType('text/*');
            type2 = matlab.net.http.MediaType('application/json','q','.5');
            acceptField = matlab.net.http.field.AcceptField([type1 type2]);
            header = [acceptField contentTypeField];
            method = matlab.net.http.RequestMethod.PUT;
            request = matlab.net.http.RequestMessage(method,header,body);

            [response,completedrequest,history] = send(request,[obj.serverIP, serverFilePath]);
        end

        function sendTextData(obj, key, val)
            data = ['{"', key , '":"', val ,'"}' ]

            body = matlab.net.http.MessageBody(data);
            body.show;
            contentTypeField = matlab.net.http.field.ContentTypeField('text/plain'); %'image/jpeg'
            type1 = matlab.net.http.MediaType('text/*');
            type2 = matlab.net.http.MediaType('application/json','q','.5');
            acceptField = matlab.net.http.field.AcceptField([type1 type2]);
            header = [acceptField contentTypeField];
            method = matlab.net.http.RequestMethod.POST;
            request = matlab.net.http.RequestMessage(method,header,body);
            show(request)

            [response,completedrequest,history] = send(request,obj.serverIP);
        end


        function data = getTextData(obj, key)
            request = matlab.net.http.RequestMessage();
            [response,completedrequest,history] = send(request,[obj.serverIP, key]);
            data = response.Body.Data;
            data = convertCharsToStrings(char(data));
        end

        function data = getFile(obj, filepath)
            request = matlab.net.http.RequestMessage();
            [response,completedrequest,history] = send(request,[obj.serverIP,'files/', filepath]);
            data = response.Body.Data;
        end
    end
end
