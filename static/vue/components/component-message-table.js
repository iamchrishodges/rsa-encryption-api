Vue.component('component-message-table',
    {
        props:['name', 'head'],
        
            
        data: function(){ 
          return {
              messages: [],
              label: 'Load'
          }  
        },
        methods:{
            reload: function(event){
                fetch("http://127.0.0.1:5000" + this.name)
                .then(response => response.json())
                .then((data) => {
                    this.messages = data
                }
                );
                this.label = 'Reload';
            }
        }
        ,
        template: `
        <div>
            <div class="card">
                <div class="card-header">
                    {{head}}
                </div>
                <div class="card-body">
        
                    <table class="table table-striped">
                        <thead>
                            <tr>
                                <th>Sender</th>
                                <th>Receiever</th>
                                <th>Message</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="m in messages">
                                <td>
                                    {{m.friend_code}}
                                </td>
                                <td>
                                    {{m.my_friend_code}}
                                </td>
                                <td>
                                    {{m.message}}
                                </td>
                            </tr>
                            <tbody>
                    </table>
                    <div>
                        <a class="btn btn-primary btn-small active" role="button" aria-pressed="true" v-on:click="reload">{{label}}</a>
                    </div>
                </div>
            </div>
        
        </div>
        `
    }
);