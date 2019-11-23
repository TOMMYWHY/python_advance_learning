window.Model = function (options) {
    let resourceName = options.resourceName // leancloud table_name
    return {
        init: function () {
            var APP_ID = 'w3uxzEnSEsFqxgNcYgdnkWAU-MdYXbMMI'
            var APP_KEY = '5IEkYert5bWRhfdHYUWXcyAi'
            AV.init({ appId: APP_ID, appKey: APP_KEY }) // leancloud database
        },
        fetch: function () {
            var query = new AV.Query(resourceName);
            return query.find() //promise
        },
        save: function (object) {
            var Instance = AV.Object.extend(resourceName);
            // var Instance = AV.Object.Query(resourceName);

            var instance = new Instance();
            // return instance.save(object)
            instance.set('username', object.username);
            instance.set('phone', object.phone);
            instance.set('email', object.email);
            instance.set('content', object.content);
            return instance.save(object)
            // return msg.save() //promise
        }
    }
}