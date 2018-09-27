Vue.component('component-friend-code',
    {
        props:['name', 'head'],
        
            
        data: function(){ 
          return {
            me: '',
            label: 'Load'
          }  
        },
        methods:{
            reload: function(event){
                fetch("http://127.0.0.1:5000" + this.name)
                .then(response => response.json())
                .then((data) => {
                    this.me = data
                
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
                    {{me.friend_code}}
                    <div>
                        <a class="btn btn-primary btn-small active" role="button" aria-pressed="true" v-on:click= "reload">{{label}}</a>
                    </div>
                </div>
            </div>
        </div>
        `
    }
);