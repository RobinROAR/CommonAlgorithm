#include <stdlib.h>
#include <stdio.h>


typedef struct node{
	int num;
	int data;
	struct node *next;
}node;

//建立链表，两个指针，p新建节点，o为前一个节点
node *create(int n){
	node *head,*o,*p;
	for(int i=0;i<n;i++){
		p = (node*)malloc(sizeof(node));
		printf("Please input node%d : ", i+1);
		scanf("%d,%d",&p->num,&p->data);
		if(i==0){
			o=p;
			head = p;
			p->next = NULL;
			}
			else{
				o->next = p;
				p->next = NULL;
				o = p;
			}
		}
	return head;

}

//释放链表， 两个指针，p为下一个节点，o为要删除的当前节点
void  drop(node *head){
	node *p,*o;
	o = p =head;
	if(head = NULL){printf("No link");exit(0);}
	while(p!=NULL){
		p=p->next;
		free(o);
		o=p;
	}
	
	if(o == NULL and p == NULL) printf("drop ok \n") ;
	else printf("wrong");
	
}	
		
//展示链表，一个指针
void show(node *head){

	node *p;
	p = head;
	while(p!=NULL){
		printf("num : %d ,data : %d  --> ", p->num,p->data);
		p = p->next;
	}
	printf(" end \n");
	p = NULL;
}

//插入链表,两个指针，o指向插入节点的前一个节点(如果是第一个需要特殊处理)
node* insert(node *head,int n){
	node *p,*o;
	o = head;
	p = (node*)malloc(sizeof(node));
		printf("Please input data after node%d: ", n);
		scanf("%d,%d",&p->num,&p->data);
	if(n==0) {
		p->next = head;
		head = p;
		
		}else{
				int i;
				for(i=0;i<n-1;i++){
					o = o->next;
					}
				p->next = o->next;
				o->next = p;
		}
	p = o =NULL;
	return head;
}

//删除节点 , 一个操作指针p， 分首节点和非首节点两种情况
node* del(node *head,int n){
	node *p;
	p = head;
	if(n==1){
		head = head->next;
		free(p);
	}
		else{
			for(int i = 2;i< n;i++){p = p->next;}
			p->next = p->next->next;
			p = p->next;
			free(p);
		}
		
	p  = NULL;
	return head;
	}		
	

//链表求长
int length(node *head){
	if(head == NULL){return 0;}
	
	int cnt=1;
	node *p;
	p = head;
	while(p->next!=NULL){
		p = p->next;
		cnt++;
	}
	p = NULL;
	return cnt;
}
	

//链表逆置，两种方法，a为标识符，0 为正常，1为递归
//正常，三个指针o,p,q ,  分别指向前中后，移动前两个
//递归，两个指针，递归子序列q
node *reverse(node *head,int a =0){
	switch(a){
		case 0:{
			if(head == NULL or head ->next == NULL) return head;
			node *o, *p ,*q;
			o = head;
			p = head->next;
			q = NULL;
			while(p!= NULL){
				q = p->next;
				p->next = o;
				o = p;
				p = q;
			}
			head->next = NULL;
			head = o;
			return head;
		}
		case 1:{
			if(head ==NULL or head->next==NULL) return head;
			node *p,*q;
			p = head;
			q = p->next;
			head = reverse(q,1);
			q->next = p;
			p->next = NULL;
			return head;
		}
	}		
	
}

	
int main(){
	printf("Please input the len of linknode: ");
	int n;
	scanf("%d", &n);
	node *head = create(n);
	show(head);
	
	int m;
	printf("where to insert : ");
	scanf("%d",&m);
	
	head = insert(head,m);
	show(head);
	
	int k;
	printf("where to del : ");
	scanf("%d",&k);
	
	head = del(head,k);
	show(head);
	
	head = reverse(head,1);
	show(head);
	
	int l = length(head);
	printf("length :  %d \n",l);
	
	drop(head);	
	scanf("%d", &n);
	return 0;	
	
	
}
